# Generated by Django 3.1.3 on 2020-12-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
