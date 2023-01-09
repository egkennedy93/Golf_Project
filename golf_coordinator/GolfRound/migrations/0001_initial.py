# Generated by Django 4.1.3 on 2023-01-09 21:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round_Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_submission_date', models.DateTimeField(default=datetime.datetime(2023, 1, 9, 21, 39, 41, 978452, tzinfo=datetime.timezone.utc))),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.golf_course')),
                ('golfer_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='accounts.golfer')),
                ('tee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.golf_tee')),
            ],
        ),
        migrations.CreateModel(
            name='Round_Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hole_1_score', models.IntegerField(default=0)),
                ('hole_2_score', models.IntegerField(default=0)),
                ('hole_3_score', models.IntegerField(default=0)),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_score', to='accounts.golfer')),
            ],
        ),
    ]
