# Generated by Django 4.1.3 on 2023-04-26 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0001_initial'),
        ('accounts', '0001_initial'),
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
            name='Trip_Golfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hcp_index', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('bet_winnings', models.DecimalField(decimal_places=4, default=0, max_digits=14, null=True)),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.golfer')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=255)),
                ('team_score', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Trip_TeeTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tee_time_date', models.DateField()),
                ('tee_time_time', models.TimeField()),
                ('gametype', models.CharField(choices=[('2v2 best ball', '2v2 best ball'), ('2v2 best ball - matchplay', '2v2 best ball - matchplay'), ('2v2 scramble', '2v2 scramble'), ('1v1 matchplay', '1v1 matchplay'), ('please select', 'please select'), ('4 person scramble', '4 person scramble')], default='please select', max_length=25)),
                ('teeTime_Complete', models.BooleanField(default=False)),
                ('Winning_Score', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('Players', models.ManyToManyField(blank=True, default='N/A', to='golf_trip.trip_golfer')),
                ('Winning_Team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.trip_team')),
                ('tee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Courses.golf_tee')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golf_trip.trip_team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golf_trip.trip_golfer')),
            ],
            options={
                'unique_together': {('team', 'user')},
            },
        ),
        migrations.AddField(
            model_name='trip_team',
            name='members',
            field=models.ManyToManyField(through='golf_trip.Trip_TeamMember', to='golf_trip.trip_golfer'),
        ),
        migrations.AddField(
            model_name='trip_team',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip'),
        ),
        migrations.CreateModel(
            name='Trip_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_time', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.trip_course')),
                ('tee_time', models.ManyToManyField(blank=True, null=True, to='golf_trip.trip_teetime')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='golf_trip.golf_trip')),
            ],
        ),
    ]
