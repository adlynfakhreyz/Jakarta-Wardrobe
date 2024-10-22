from django.core.management.base import BaseCommand
import pandas as pd
from products.models import Product
import uuid

class Command(BaseCommand):
    help = 'Import products from an Excel file into the database.'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='C:\\Users\\sayyi\\Downloads\\Dataset.xlsx')

    def handle(self, *args, **options):
        # Load the data into a pandas DataFrame
        data = pd.read_excel(options['filepath'], engine='openpyxl')
        
        # Iterate through the rows of the DataFrame, creating Product instances
        for _, row in data.iterrows():
            Product.objects.update_or_create(
                uuid=uuid.uuid4(),
                defaults={
                    'category': row['category'],
                    'name': row['name'],
                    'price': row['price'],
                    'desc': row['desc'],
                    'color': row['color'],
                    'stock': row['stock'],
                    'shop_name': row['shop_name'],
                    'location': row['location'],
                    'img_url': row['img_url'],
                }
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully imported products from {options["filepath"]}'))
