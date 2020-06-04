from locations.models import Country, City
from rest_framework import serializers
from django.contrib.auth.models import User


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country', read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class CountriesSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = Country
        fields = '__all__'

class QuerySerializer(serializers.Serializer):
    country_id = serializers.IntegerField()

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user