# Generated by Django 4.1.3 on 2023-01-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf_trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip_teetime',
            name='Players',
            field=models.ManyToManyField(blank=True, to='golf_trip.trip_golfer'),
        ),
    ]
