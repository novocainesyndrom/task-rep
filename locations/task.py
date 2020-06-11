from django.urls import reverse
from django.core.mail import send_mail
from task_7.celery import app
from django.shortcuts import get_object_or_404

@app.task
def send_add_country_email(recipient_list):
    send_mail(
            'Adding country',
            "Congratulations! Your country was successfully added!\n",
            'from@locations.dev',
            recipient_list,
            fail_silently=False,
        )


@app.task
def send_edit_country_email(recipient_list, country_id):
    from .models import Country

    country = get_object_or_404(Country, id=country_id)
    print("recipient_list", recipient_list)
    send_mail(
            'Editing country',
            f"Your country {country} was changed. You can view changes at "\
            f"http://127.0.0.1:8000{reverse('locations:country_page', args=[country.id])}",
            'from@locations.dev',
            recipient_list,
            fail_silently=False,
        )


@app.task
def print_to_shell():
    print('It\'s about time')