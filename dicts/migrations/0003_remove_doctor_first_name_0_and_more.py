# Generated by Django 4.2.3 on 2023-08-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicts', '0002_hospital_city_alter_education_institution_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='first_name_0',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='first_name_1',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='first_name_2',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name_0',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name_1',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name_2',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='middle_name_0',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='middle_name_1',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='middle_name_2',
        ),
        migrations.AddField(
            model_name='doctor',
            name='fullname_0',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fullname_1',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fullname_2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
