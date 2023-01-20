# Generated by Django 4.1.3 on 2023-01-20 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GolfRound', '0002_alter_round_submission_round_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='round_score',
            name='hole_10_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_11_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_12_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_13_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_14_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_15_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_16_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_17_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_18_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_4_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_5_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_6_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_7_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_8_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='hole_9_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='net_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round_score',
            name='total_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='round_score',
            name='hole_1_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='round_score',
            name='hole_2_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='round_score',
            name='hole_3_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='round_submission',
            name='round_submission_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 16, 28, 24, 862615, tzinfo=datetime.timezone.utc)),
        ),
    ]
