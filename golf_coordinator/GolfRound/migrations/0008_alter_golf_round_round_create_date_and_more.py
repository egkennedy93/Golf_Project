# Generated by Django 4.1.3 on 2023-01-06 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GolfRound', '0007_alter_golf_round_round_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golf_round',
            name='round_create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 16, 33, 51, 481372, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='round_submission',
            name='round_submission_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 16, 33, 51, 481919, tzinfo=datetime.timezone.utc)),
        ),
    ]