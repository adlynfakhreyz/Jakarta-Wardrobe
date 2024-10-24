# Generated by Django 5.1.1 on 2024-10-22 14:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desc', models.TextField(blank=True, null=True)),
                ('color', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('shop_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=255)),
                ('img_url', models.URLField(max_length=500)),
            ],
        ),
    ]
