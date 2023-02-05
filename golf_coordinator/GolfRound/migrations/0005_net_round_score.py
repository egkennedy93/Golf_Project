# Generated by Django 4.1.3 on 2023-01-28 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GolfRound', '0004_round_score_golfer_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Net_Round_Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_golfer', models.CharField(max_length=255)),
                ('hole_1_score', models.IntegerField()),
                ('hole_2_score', models.IntegerField()),
                ('hole_3_score', models.IntegerField()),
                ('hole_4_score', models.IntegerField()),
                ('hole_5_score', models.IntegerField()),
                ('hole_6_score', models.IntegerField()),
                ('hole_7_score', models.IntegerField()),
                ('hole_8_score', models.IntegerField()),
                ('hole_9_score', models.IntegerField()),
                ('hole_10_score', models.IntegerField()),
                ('hole_11_score', models.IntegerField()),
                ('hole_12_score', models.IntegerField()),
                ('hole_13_score', models.IntegerField()),
                ('hole_14_score', models.IntegerField()),
                ('hole_15_score', models.IntegerField()),
                ('hole_16_score', models.IntegerField()),
                ('hole_17_score', models.IntegerField()),
                ('hole_18_score', models.IntegerField()),
                ('total_score', models.IntegerField()),
                ('net_score', models.IntegerField()),
                ('raw_round_score', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GolfRound.round_score')),
            ],
        ),
    ]
