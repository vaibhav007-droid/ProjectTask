# Generated by Django 3.1.3 on 2020-12-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
