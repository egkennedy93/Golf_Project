# Generated by Django 4.1.3 on 2023-01-06 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GolfRound', '0003_golf_round_course_alter_golf_round_round_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golf_round',
            name='round_create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 13, 48, 54, 458013, tzinfo=datetime.timezone.utc)),
        ),
    ]
