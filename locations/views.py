from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('locations:login'))

@login_required
def countries_page(request):
    countries = Country.objects.all()
    content = {'countries': countries,
               'user':request.user}
    return render(request, 'locations/countries_page.html', content)

@login_required
def country_page(request, country):
    countries = [country.name for country in Country.objects.all()]
    if country not in countries:
        raise Http404

    cities = [city for city in City.objects.all() if city.country.name == country]
    content = {'country':country,
               'cities': cities,
               'user':request.user}
    return render(request, 'locations/country_page.html', content)

@login_required
def city(request,country, city_name):
    cities = [city.name for city in City.objects.all() if city.country.name == country]
    if city_name not in cities:
        raise Http404

    city_obg = City.objects.get(name=city_name)
    content = {'city': city_obg,
               'user':request.user}
    return render(request, 'locations/city.html', content)

@login_required
def remove_city(request, city_name):
    city = City.objects.get(name=city_name)
    country = city.country.name
    city.delete()
    return HttpResponseRedirect(reverse('locations:country_page',
                                        args=[country]
                                        ))

