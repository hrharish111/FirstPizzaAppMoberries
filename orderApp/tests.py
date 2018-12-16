from decimal import Decimal
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.


class TestingOrders(APITestCase):
    def testingOrderDetails(self):
        self.url =reverse('order-list')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class TestingItemList(APITestCase):
    def testingDeleteItemList(self):
        self.details_url = reverse('orderitems-detail',kwargs={'pk':3})
        response = self.client.delete(self.details_url,{})
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)