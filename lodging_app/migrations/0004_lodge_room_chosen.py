# Generated by Django 4.2.2 on 2023-07-04 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_owner_utility_image1_owner_utility_image2_and_more'),
        ('lodging_app', '0003_remove_lodge_image1_remove_lodge_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodge',
            name='room_chosen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu_app.owner_utility'),
            preserve_default=False,
        ),
    ]