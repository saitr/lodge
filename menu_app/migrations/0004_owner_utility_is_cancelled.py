# Generated by Django 4.2.2 on 2023-07-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0003_owner_utility_is_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_utility',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
