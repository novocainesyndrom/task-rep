from django.utils.deprecation import MiddlewareMixin
from .models import Country

class GetCountry(MiddlewareMixin):

    def process_request(self, request):

        country_list = Country.objects.all()
        request.country_list = country_list
        return None
