# Generated by Django 4.1.3 on 2023-02-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf_trip', '0004_trip_teetime_teetime_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip_golfer',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
