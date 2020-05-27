from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete


class Symbol(models.Model):
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.image.url


class Country(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=True, default='No description' )
    population = models.IntegerField(default=0)
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE, related_name='symbol')
    cities_count = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name="users")

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        verbose_name_plural = 'Cities'

    def pre_add_city(instance, **kwargs):
        print('City is added')


    def post_add_city(instance, **kwargs):
        cities = instance.country
        cities.cities_count += 1
        cities.save()

    def pre_delete_city(instance, **kwargs):
        cities = instance.country
        cities.cities_count -= 1
        cities.save()



    def post_delete_city(instance, **kwargs):
        print('City is deleted')


    def __str__(self):
        return self.name

pre_save.connect(City.pre_add_city, sender=City)
post_save.connect(City.post_add_city, sender=City)
pre_delete.connect(City.pre_delete_city, sender=City)
post_delete.connect(City.post_delete_city, sender=City)