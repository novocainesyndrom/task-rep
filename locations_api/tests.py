from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from locations.models import *
from django.core.files import File
import pathlib


class AccountTests(APITestCase):
    def setUp(self):
        image_file = File(open(f'{pathlib.Path().absolute()}/media/roger.jpeg', 'rb'))
        self.user = User.objects.create_user(username='admin',password='12345')
        self.user.save()
        flag = Symbol.objects.create(image=image_file)
        flag.save()
        self.country = Country.objects.create(name='Libertalia', population=2, flag=flag)
        self.country.save()
        self.country.users.add(self.user)
        self.city = City.objects.create(name='Newport',longitude=15, latitude=16, country=self.country)
        self.city.save()
        self.client.force_authenticate(self.user)

    def test_create_account(self):

        url = reverse('create_user')
        data = {'username': 'john', 'password':'12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(User.objects.all()), 2)
        self.assertEqual(User.objects.get(id=2).username, 'john')

    def test_show_country(self):
        url = reverse('country', args=[self.country.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(City.objects.all().filter(country__id=self.country.id)), 1)

    def test_edit_city(self):
        url = reverse('city', args=[self.city.id])
        new_longitude = 38
        response = self.client.patch(url, {'longitude':new_longitude})
        self.assertEqual(new_longitude, response.data['longitude'])

