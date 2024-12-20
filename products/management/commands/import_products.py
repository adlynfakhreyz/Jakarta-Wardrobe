from django.core.management.base import BaseCommand
import pandas as pd
from products.models import Product
import uuid

class Command(BaseCommand):
    help = 'Import products from Dataset.xlsx into the database.'

    def handle(self, *args, **options):
        # Define the file path
        filepath = 'Dataset.xlsx'
        
        # Load the data into a pandas DataFrame
        data = pd.read_excel(filepath)
        
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
        self.stdout.write(self.style.SUCCESS(f'Successfully imported products from {filepath}'))
