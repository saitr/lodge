# Generated by Django 4.2.2 on 2023-07-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0007_alter_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
