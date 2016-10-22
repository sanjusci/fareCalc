'''
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(urlpatterns)
'''
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^api/v1/location/$', views.AddressLocation.as_view(), name='address-location'),
    url(r'^api/v1/fare/$', views.FareDetail.as_view(), name='fare-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
