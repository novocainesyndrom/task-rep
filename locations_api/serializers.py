from locations.models import Country, City
from rest_framework import serializers



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

