# Generated by Django 4.1.3 on 2023-01-09 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_alter_golfer_hcp_index'),
        ('teams', '0004_alter_team_name'),
        ('Courses', '0006_alter_golf_tee_tee_name_alter_golf_tee_9_hole_course_and_more'),
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
            name='Trip_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Courses.golf_course')),
                ('tee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Courses.golf_tee')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_score', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.team')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Golfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.golfer')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teams.team')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tee_time', models.DateTimeField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.trip_course')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
    ]
