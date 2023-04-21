# Generated by Django 4.1.3 on 2023-04-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf_trip', '0002_trip_golfer_bet_winnings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip_golfer',
            name='bet_winnings_currency',
        ),
        migrations.AlterField(
            model_name='trip_golfer',
            name='bet_winnings',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=14, null=True),
        ),
    ]
