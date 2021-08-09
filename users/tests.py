from django.test import TestCase
from rest_framework.test import APIRequestFactory

# Create your tests here.
factory = APIRequestFactory()
request = factory.post('/users/', {'username': 'GG','email':'gordon@gordon.com', 'password':'ilovekibbles'},format='json')