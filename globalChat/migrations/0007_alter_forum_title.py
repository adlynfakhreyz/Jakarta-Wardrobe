# Generated by Django 5.1.2 on 2024-10-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalChat', '0006_alter_forum_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='title',
            field=models.CharField(max_length=75),
        ),
    ]