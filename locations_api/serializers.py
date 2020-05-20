from locations.models import Country
from rest_framework import serializers


class CountrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Country
        fields = ['name','cities_count', 'population', 'description']

