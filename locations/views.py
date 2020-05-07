from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
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
def country_page(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    cities = [city for city in City.objects.all() if city.country.id == country_id]
    content = {'country':country,
               'cities': cities,
               'user':request.user}
    return render(request, 'locations/country_page.html', content)

@login_required
def city(request, city_id):
    city_obg =  get_object_or_404(City, id=city_id)
    content = {'city': city_obg,
               'user':request.user}
    return render(request, 'locations/city.html', content)

@login_required
def remove_city(request, city_id):
    city_obg =  get_object_or_404(City, id=city_id)
    country = city_obg.country.id
    city_obg.delete()
    return HttpResponseRedirect(reverse('locations:country_page',
                                        args=[country]
                                        ))

