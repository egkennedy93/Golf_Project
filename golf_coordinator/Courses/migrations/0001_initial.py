# Generated by Django 4.1.3 on 2023-04-26 13:50

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
            name='Golf_Tee_9_Hole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tee_name', models.CharField(max_length=255)),
                ('course_par', models.IntegerField()),
                ('yardage', models.IntegerField()),
                ('hole_1_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_1_yardage', models.IntegerField(default=0)),
                ('hole_1_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_2_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_2_yardage', models.IntegerField(default=0)),
                ('hole_2_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_3_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_3_yardage', models.IntegerField(default=0)),
                ('hole_3_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_4_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_4_yardage', models.IntegerField(default=0)),
                ('hole_4_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_5_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_5_yardage', models.IntegerField(default=0)),
                ('hole_5_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_6_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_6_yardage', models.IntegerField(default=0)),
                ('hole_6_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_7_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_7_yardage', models.IntegerField(default=0)),
                ('hole_7_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_8_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_8_yardage', models.IntegerField(default=0)),
                ('hole_8_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_9_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_9_yardage', models.IntegerField(default=0)),
                ('hole_9_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('course', models.ForeignKey(default='please select', on_delete=django.db.models.deletion.CASCADE, related_name='golf_tees_9', to='Courses.golf_course')),
            ],
        ),
        migrations.CreateModel(
            name='Golf_Tee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tee_name', models.CharField(max_length=255)),
                ('course_par', models.IntegerField()),
                ('slope', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('yardage', models.IntegerField()),
                ('hole_1_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_1_yardage', models.IntegerField(default=0)),
                ('hole_1_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_2_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_2_yardage', models.IntegerField(default=0)),
                ('hole_2_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_3_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_3_yardage', models.IntegerField(default=0)),
                ('hole_3_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_4_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_4_yardage', models.IntegerField(default=0)),
                ('hole_4_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_5_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_5_yardage', models.IntegerField(default=0)),
                ('hole_5_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_6_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_6_yardage', models.IntegerField(default=0)),
                ('hole_6_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_7_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_7_yardage', models.IntegerField(default=0)),
                ('hole_7_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_8_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_8_yardage', models.IntegerField(default=0)),
                ('hole_8_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_9_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_9_yardage', models.IntegerField(default=0)),
                ('hole_9_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_10_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_10_yardage', models.IntegerField(default=0)),
                ('hole_10_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_11_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_11_yardage', models.IntegerField(default=0)),
                ('hole_11_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_12_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_12_yardage', models.IntegerField(default=0)),
                ('hole_12_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_13_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_13_yardage', models.IntegerField(default=0)),
                ('hole_13_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_14_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_14_yardage', models.IntegerField(default=0)),
                ('hole_14_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_15_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_15_yardage', models.IntegerField(default=0)),
                ('hole_15_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_16_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_16_yardage', models.IntegerField(default=0)),
                ('hole_16_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_17_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_17_yardage', models.IntegerField(default=0)),
                ('hole_17_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('hole_18_par', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=4)),
                ('hole_18_yardage', models.IntegerField(default=0)),
                ('hole_18_index', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], default=1)),
                ('course', models.ForeignKey(default='please select', on_delete=django.db.models.deletion.CASCADE, related_name='golf_tees', to='Courses.golf_course')),
            ],
            options={
                'unique_together': {('course', 'tee_name')},
            },
        ),
    ]
