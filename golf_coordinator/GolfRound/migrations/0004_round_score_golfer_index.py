# Generated by Django 4.1.3 on 2023-01-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GolfRound', '0003_remove_round_score_submission_round_score_tee_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='round_score',
            name='golfer_index',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]
