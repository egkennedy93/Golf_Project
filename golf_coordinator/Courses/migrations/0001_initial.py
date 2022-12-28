# Generated by Django 4.1.3 on 2022-12-28 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Golf_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Golf_Tee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('golf_tee_name', models.CharField(max_length=255, unique=True)),
                ('course_par', models.IntegerField()),
                ('slope', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('yardage', models.IntegerField()),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.golf_course')),
            ],
            options={
                'unique_together': {('course_name', 'golf_tee_name')},
            },
        ),
        migrations.CreateModel(
            name='Golf_Hole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hole_number', models.IntegerField()),
                ('par', models.IntegerField()),
                ('yardage', models.IntegerField()),
                ('hcp_index', models.IntegerField()),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hole_course', to='Courses.golf_course')),
                ('referred_tee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hole_tee', to='Courses.golf_tee')),
            ],
            options={
                'unique_together': {('course_name', 'referred_tee_name', 'hole_number')},
            },
        ),
    ]
