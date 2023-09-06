# Generated by Django 4.2.3 on 2023-08-24 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dicts', '0007_surgerytype'),
        ('surgery', '0003_alter_patientsurgery_medicine_description_0_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsurgery',
            name='surgery_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='surgery_patient_surgery_type', to='dicts.surgerytype'),
        ),
    ]
