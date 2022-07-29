from rest_framework.test import APITestCase

from apps.auto_parks.models import AutoParksModel
from django.urls import reverse
from rest_framework import status

from apps.cars.models import CarModel


class AutoParkTestCase(APITestCase):
    def authenticate(self):
        user = {
            'email': 'admin@gmail.com',
            'password': 'P@$$word1',
            'profile': {
                'name': 'Max',
                'surname': 'Popov',
                'age': 18,
                'phone': '0949642513'
            }
        }
        self.client.post(reverse('users_list_create'), user, format='json')
        response = self.client.post(reverse('auth_login'), {'email': 'admin@gmail.com', 'password': 'P@$$word1'})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

    def test_create_auto_park_without_auth(self):
        prev_count = AutoParksModel.objects.count()
        sample_auto_park = {
            'name': 'Uber'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(AutoParksModel.objects.count(), prev_count)

    def test_create_auto_park(self):
        self.authenticate()
        prev_count = AutoParksModel.objects.count()
        sample_auto_park = {
            'name': 'Uber'
        }

        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Uber')
        self.assertEqual(AutoParksModel.objects.count(), prev_count + 1)
        self.assertIsInstance(response.data['cars'], list)

    def test_add_car(self):
        self.authenticate()
        prev_count = CarModel.objects.count()
        sample_car = {
            'brand': 'BMW',
            'price': 2000,
            'year': 2000
        }
        sample_auto_park = {
            'name': 'Uber'
        }
        pk = self.client.post(reverse('auto_parks_list_create'), sample_auto_park).data['id']
        response = self.client.post(reverse('auto_parks_add_car', args=(pk,)), sample_car)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['brand'], 'BMW')
        self.assertEqual(response.data['price'], 2000)
        self.assertEqual(response.data['year'], 2000)
        self.assertEqual(CarModel.objects.count(), prev_count + 1)
