# Generated by Django 4.1.3 on 2023-01-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf_trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip_team',
            name='team_score',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
