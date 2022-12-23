# Generated by Django 4.1.3 on 2022-12-23 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Golf_Course',
        ),
        migrations.RenameField(
            model_name='golf_tee',
            old_name='color',
            new_name='tee_color',
        ),
        migrations.RenameField(
            model_name='golf_tee',
            old_name='name',
            new_name='tee_name',
        ),
        migrations.AlterUniqueTogether(
            name='golf_tee',
            unique_together={('course', 'tee_color')},
        ),
    ]