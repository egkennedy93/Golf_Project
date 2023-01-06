# Generated by Django 4.1.3 on 2023-01-06 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0003_alter_golf_tee_course'),
        ('accounts', '0003_alter_golfer_picture'),
        ('teams', '0002_teammember_delete_groupmember_alter_team_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Golf_Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_date', models.DateField()),
                ('trip_name', models.CharField(max_length=255)),
                ('trip_description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.team')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Golfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.golfer')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.team')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Courses.golf_course')),
                ('tee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Courses.golf_tee')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
    ]
