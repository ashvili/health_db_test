# Generated by Django 4.2.3 on 2023-08-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surgery', '0002_alter_patientsurgery_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsurgery',
            name='medicine_description_0',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientsurgery',
            name='medicine_description_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientsurgery',
            name='medicine_description_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
