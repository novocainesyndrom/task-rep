from django.core.management.base import BaseCommand
import sys, re
from locations.models import Country

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('string', type=str)

    def handle(self, *args, **kwargs):
        string = sys.argv[2]
        countries = [country.name for country in Country.objects.all()]
        for country in countries:
            self.stdout.write(
            f"'{string}' in {country}'s name" if re.search(string,country) else f"'{string}' not in {country}'s name"
            )