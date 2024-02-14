import csv
import os
from calculator_app.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import products from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        csv_file_path = os.path.abspath(csv_file_path)

        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                _, created = Product.objects.get_or_create(
                    name=row[1],
                    serving_size=row[2][:-1],
                    calories=row[3],
                    protein=row[38][:-1],
                    carbohydrate=row[58][:-1],
                    fat=row[67][:-1],
                )

        self.stdout.write(self.style.SUCCESS('Products imported successfully'))