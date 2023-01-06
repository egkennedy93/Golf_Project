# Generated by Django 4.1.3 on 2023-01-06 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_alter_golfer_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('team_score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('members', models.ManyToManyField(through='teams.GroupMember', to='accounts.golfer')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='groupmember',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='teams.team'),
        ),
        migrations.AddField(
            model_name='groupmember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_groups', to='accounts.golfer'),
        ),
        migrations.AlterUniqueTogether(
            name='groupmember',
            unique_together={('group', 'user')},
        ),
    ]
