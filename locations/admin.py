from django.contrib import admin
from locations.models import Symbol, Country, City

@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_filter = ['country']

admin.site.register(Symbol)
