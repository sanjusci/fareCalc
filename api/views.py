# Create your views here.

from api.models import Address
from rest_framework import generics
from django.contrib.auth.models import User

from api.serializers import UserSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView

#Creating an endpoint for the root of our API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.permissions import IsOwnerOrReadOnly
from api.serializers import AddressSerializer,LocationSerializer
import json, requests
from django.conf import settings

class AddressLocation(generics.CreateAPIView):
    serializer_class = AddressSerializer
    
    def post(self, request, *args, **kwargs):
		address = (request.data.get('address', ''))
		if not address:
			return Response('Address Required', status=status.HTTP_400_BAD_REQUEST)
		url = settings.ZOMATO_API_URL + 'locations'
		data = {'query': address}
		headers = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user-key": settings.ZOMATO_KEY}
		r = requests.get(url,headers=headers, params=data)
		assert r.status_code == 200
		try:
			res = json.loads(r.text)
			for x in res['location_suggestions']:
				entity_id = x['entity_id']
				entity_type = x['entity_type'].encode('utf8')
		except (ValueError, KeyError, TypeError):
			Response('Zomato api response error', status=status.HTTP_400_BAD_REQUEST)
			pass
		self.create(request, *args, **kwargs)
		return Response({'entity_id':entity_id, 'entity_type' : entity_type})
         
class FareDetail(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

    def list(self, request, *args, **kwargs):
		all_lat_longs = []
		fare_details = []
		prices_details = []
		start_lat = None
		start_lon = None
		entity_id = request.query_params.get('entity_id', '')
		entity_type = request.query_params.get('entity_type', '')
		url = settings.ZOMATO_API_URL + 'location_details'
		uber_url = settings.UBER_API_BASE_URL + 'estimates/price'
		data = {'entity_id': entity_id, 'entity_type' : entity_type}
		headers = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user-key": settings.ZOMATO_KEY}
		zomato_resp = requests.get(url, headers=headers, params=data, verify=False)
		if zomato_resp.status_code == 200:
			res_data = zomato_resp.json()
			start_lat = float(res_data['location']['latitude'])
			start_lon = float(res_data['location']['longitude'])
			for best_rest in res_data.get('best_rated_restaurant', []):
				end_lat = float(best_rest['restaurant']['location']['latitude'])
				end_lon = float(best_rest['restaurant']['location']['longitude'])
				param = {
				'server_token': settings.UBER_KEY,
				'start_longitude': start_lon,
				'end_longitude': end_lon,
				'start_latitude':start_lat,
				'end_latitude': end_lat}
				
				res = requests.get(uber_url, params=param, verify=False)
				if res.status_code == 200:
					resp = res.json()
					fare_details.append({
					'restaurant_name': best_rest['restaurant']['name'],
					'restaurant_address': best_rest['restaurant']['location']['address'],
					'low_price': resp['prices'][0]['low_estimate'],
					'max_price': resp['prices'][0]['high_estimate'],
					'service_name':resp['prices'][0]['localized_display_name']
					})
			fare_details = sorted(fare_details, key=lambda k: k['low_price'])
		return Response({"fare_details": fare_details})
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'api': reverse('address-location', request=request, format=format)
    })
