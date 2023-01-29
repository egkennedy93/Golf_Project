# Generated by Django 4.1.3 on 2023-01-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf_trip', '0002_remove_trip_golfer_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip_teetime',
            name='gametype',
            field=models.CharField(choices=[('2v2 best ball', '2v2 best ball'), ('2v2 best ball - matchplay', '2v2 best ball - matchplay'), ('2v2 scramble', '2v2 scramble'), ('1v1 matchplay', '1v1 matchplay'), ('please select', 'please select'), ('4 person scramble', '4 person scramble')], default='please select', max_length=25),
        ),
    ]
