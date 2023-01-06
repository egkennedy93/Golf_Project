# Generated by Django 4.1.3 on 2023-01-06 17:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0003_alter_golf_tee_course'),
        ('GolfRound', '0008_alter_golf_round_round_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golf_round',
            name='round_create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 17, 30, 9, 828563, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='round_submission',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.golf_course'),
        ),
        migrations.AlterField(
            model_name='round_submission',
            name='round_submission_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 17, 30, 9, 829151, tzinfo=datetime.timezone.utc)),
        ),
    ]