# Generated by Django 4.1.3 on 2023-04-26 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('golf_trip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GolfBet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bet_closed', models.BooleanField(default=False)),
                ('test', models.CharField(default='test', max_length=500)),
                ('bet_winner', models.ForeignKey(blank=True, default='N/A', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='winner', to='golf_trip.trip_golfer')),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opponent', to='golf_trip.trip_golfer')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submitter', to='golf_trip.trip_golfer')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdPartyPlayerVsPlayer',
            fields=[
                ('golfbet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookie.golfbet')),
                ('opponent_tee_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_2_tee_time', to='golf_trip.trip_teetime')),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_1', to='golf_trip.trip_golfer')),
                ('player_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_2', to='golf_trip.trip_golfer')),
                ('submitter_tee_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_1_tee_time', to='golf_trip.trip_teetime')),
            ],
            bases=('bookie.golfbet',),
        ),
        migrations.CreateModel(
            name='TeeTimeBet',
            fields=[
                ('golfbet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookie.golfbet')),
                ('bet_tee_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bet_tee_time', to='golf_trip.trip_teetime')),
            ],
            bases=('bookie.golfbet',),
        ),
        migrations.CreateModel(
            name='TeamVsTeam',
            fields=[
                ('golfbet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookie.golfbet')),
                ('submitter_selected_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submitter_selected_team', to='golf_trip.trip_team')),
                ('tee_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='TVT_submitter_tee_time', to='golf_trip.trip_teetime')),
            ],
            bases=('bookie.golfbet',),
        ),
        migrations.CreateModel(
            name='PlayerVsPlayer',
            fields=[
                ('golfbet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookie.golfbet')),
                ('opponent_tee_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opponent_tee_time', to='golf_trip.trip_teetime')),
                ('submitter_tee_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PVP_submitter_tee_time', to='golf_trip.trip_teetime')),
            ],
            bases=('bookie.golfbet',),
        ),
    ]
