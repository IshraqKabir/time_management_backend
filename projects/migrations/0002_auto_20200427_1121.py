# Generated by Django 3.0 on 2020-04-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_date_month',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_date_year',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date_day',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='estimated_time_hours',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='estimated_time_mins',
            field=models.IntegerField(blank=True),
        ),
    ]