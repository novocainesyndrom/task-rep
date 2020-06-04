from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.utils import json
from rest_framework.views import APIView
from .serializers import *
from locations.models import Country, City
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

class CountriesView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [IsAuthenticated]


class CountryView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [IsAuthenticated]


class CitiesView(ListCreateAPIView):
    queryset = City.objects.all().order_by('country__id')
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        qry_serial = QuerySerializer(data=self.request.query_params)
        qry_serial.is_valid(raise_exception=True)
        query_data = self.queryset.filter(country__id=qry_serial.validated_data.get('country_id'))
        return query_data



class CityView(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]



class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerial
    permission_classes = [AllowAny]


    def post(self,  request, *args, **kwargs):
        serializer = UserSerial(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)
        response = {}
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)
