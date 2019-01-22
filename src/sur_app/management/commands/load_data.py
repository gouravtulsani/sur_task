from django.core.management.base import BaseCommand
import csv
from sur_app.models import AdultData

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('audit_data.csv', 'r') as ip_file:
            reader = csv.reader(ip_file)
            for row in reader:
                print(row)
                _, created = AdultData.objects.get_or_create(
                    age = int(row[0]),
                    work_class = row[1],
                    fnlwgt = int(row[2]),
                    education = row[3],
                    ed_no = int(row[4]),
                    marital_status = row[5],
                    occupation = row[6],
                    relationship = row[7],
                    race = row[8],
                    sex = row[9],
                    capital_gain = int(row[10]),
                    capital_loss = int(row[11]),
                    hours_per_week = int(row[12]),
                    native_country = row[13],
                    income_range = row[14]
                )
