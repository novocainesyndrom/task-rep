from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from locations.models import Country, City


class CountriesView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer


class CountryView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer



class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('country__id')
    serializer_class = CitySerializer

    def get_queryset(self):

        country_id = self.request.query_params.get('order', None)
        if country_id is not None:
            self.queryset = self.queryset.filter(country__id=country_id)
        return self.queryset



