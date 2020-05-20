from rest_framework import viewsets
from .serializers import *
from locations.models import Country


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer

