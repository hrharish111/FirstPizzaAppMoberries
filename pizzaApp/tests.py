from decimal import Decimal
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


# Create your tests here.
class TestingPizzaSize(APITestCase):
    def testingCreatePizza(self):
        self.url = reverse('pizzasize-list')
        self.newsize = {'size':1000}
        response = self.client.post(self.url,self.newsize)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class TestingPizzaApp(APITestCase):
    def test_all_list_pizza(self):
        self.url = reverse('pizza-list')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class TestingPizzaVariationApp(APITestCase):
    def testingUpdateVariation(self):
        self.variation = {
            'price':Decimal(12.00)
        }
        self.details = reverse('pizzavariation-detail',kwargs={'pk':1})
        response = self.client.put(self.details,self.variation)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)