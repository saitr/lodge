# Generated by Django 4.2.2 on 2023-07-04 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_owner_utility_image1_owner_utility_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_utility',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]