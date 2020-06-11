from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
#from locations.task import send_add_country_email, send_edit_country_email

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
    cities = City.objects.filter(country=country)
    content = {'country':country,
               'cities': cities}
    return render(request, 'locations/country_page.html', content)

@login_required
def city(request, city_id):
    city_obg =  get_object_or_404(City, id=city_id)
    content = {'city': city_obg}
    return render(request, 'locations/city.html', content)

@login_required
def remove_city(request, city_id):
    city_obg =  get_object_or_404(City, id=city_id)
    country = city_obg.country.id
    city_obg.delete()
    return HttpResponseRedirect(reverse('locations:country_page',
                                        args=[country]
                                        ))

@login_required
def add_country(request):
    if request.method != "POST":
        form = CountryForm()
    else:
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            flag = Symbol.objects.create(
                image=request.FILES['flag_image']
            )
            new_country = form.save(commit=False)
            new_country.flag = flag
            new_country.save()
            new_country.users.add(request.user)
            #send_add_country_email.delay([request.user.email])
            return HttpResponseRedirect(reverse('locations:countries_page'))

    context = {'form': form}
    return render(request, 'locations/add_country.html', context)

@login_required
def add_city(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    if request.method != "POST":
        form = CityForm()
    else:
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.save(commit=False)
            new_city.country = country
            new_city.save()
            return HttpResponseRedirect(reverse('locations:country_page',
                                        args=[country.id]))

    context = {'form': form,
               'country':country}
    return render(request, 'locations/add_city.html', context)

@login_required
def edit_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    if request.method != "POST":
        form = CountryForm(instance=country)
    else:
        form = CountryForm(request.POST, request.FILES, instance=country )
        if form.is_valid():
            flag = Symbol.objects.create(
                image=request.FILES['flag_image']
            )
            new_country = form.save(commit=False)
            new_country.flag = flag
            form.save()
            #send_edit_country_email.delay([request.user.email], new_country.id)
            return HttpResponseRedirect(reverse('locations:countries_page'))

    content = {'form': form,
               'country': country}
    return render(request, 'locations/edit_country.html', content)

@login_required
def edit_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    if request.method != "POST":
        form = CityForm(instance=city)
    else:
        form = CityForm(instance=city, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('locations:country_page',
                                        args=[city.country.id]))

    content = {'form': form,
               'city': city}
    return render(request, 'locations/edit_city.html', content)
