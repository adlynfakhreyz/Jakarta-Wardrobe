# Generated by Django 5.1.2 on 2024-10-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalChat', '0005_forum_bookmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
