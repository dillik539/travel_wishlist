# Generated by Django 2.0.3 on 2018-03-25 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0002_auto_20180325_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='date_visited',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
