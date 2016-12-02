Requirements
   Python (2.7, 3.2, 3.3, 3.4, 3.5)
   Django (1.8, 1.9, 1.10)

Installation

Install using pip...

pip install djangorestframework

Add 'rest_framework' to your INSTALLED_APPS setting.

INSTALLED_APPS = (
    ...
    'rest_framework',
)
Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups.

Startup up a new project like so...

pip install django
pip install djangorestframework
django-admin.py startproject example .
./manage.py migrate
./manage.py createsuperuser

# fareCalc
Problem Statements for Code
PROBLEM 1: Food Tripping!
Aim: Make a backend, which takes input of a given address. Using this input, it finds the list of nearest 10 best restaurants (using Zomato API), and calculates the taxi fare to go to each restaurant (using Uber API). The output contains a list of the restaurants, along with the taxi fare needed to get to each of them.
API endpoints needed for the user:
Step 1: User will make a POST request to the API, containing the address. The address gets stored in the DB, and returns the location ID to the user
Sample endpoint: /POST api/v1/location
Sample input: Greater Kailash (GK) 2, New Delhi
Step 2: User makes a GET request to the API, containing the location ID, and gets a list of 10 restaurants, with the rating for each restaurant, along with the taxi fare, sorted in ascending order from lowest fare to highest fare
Sample endpoint: /GET /api/v1/fare/<location_id>
Reference Material:
Zomato API:
To get the location info: https://developers.zomato.com/documentation#!/location/locations
To get the best restaurants for a location: https://developers.zomato.com/documentation#!/location/location_details
Uber API:
To get fare: https://developer.uber.com/docs/ride-requests/references/api/v1-estimates-price-get
Estimate: 4 hours
PROBLEM 2: Optimize Optimize Optimize!
Aim: Find out the maximum sub-array of non negative numbers from an array, in the manner which uses the least computation and memory effort.
This problem can easily be done in O(n^3), but we are looking for a O(n) implementation, or at least a O(n^2)
Details:
The sub-array should be continuous, i.e. a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than Sub-array B if sum(A) > sum(B).
Example:
A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5], [2, 3]
The answer is [1, 2, 5], as its sum is larger than [2, 3]
NOTE #1: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE #2: If there is still a tie, then return the segment with minimum starting index
Estimate: 2 hour
