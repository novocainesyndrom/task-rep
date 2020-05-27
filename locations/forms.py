from django import forms
from .models import *

class CountryForm(forms.ModelForm):

	flag_image = forms.ImageField()
	class Meta:
		model = Country
		exclude = ['flag', 'users']


class CityForm(forms.ModelForm):
	class Meta:
		model = City
		exclude = ['country']

