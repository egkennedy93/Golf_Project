# Generated by Django 4.1.3 on 2023-01-13 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GolfRound', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round_submission',
            name='round_submission_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 0, 9, 54, 759339, tzinfo=datetime.timezone.utc)),
        ),
    ]
