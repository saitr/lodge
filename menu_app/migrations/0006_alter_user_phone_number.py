# Generated by Django 4.2.2 on 2023-07-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0005_owner_utility_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
