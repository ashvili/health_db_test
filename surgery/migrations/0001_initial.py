# Generated by Django 4.2.3 on 2023-08-07 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0004_remove_patient_first_name_0_and_more'),
        ('dicts', '0003_remove_doctor_first_name_0_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientSurgery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('diagnosis_0', models.CharField(blank=True, max_length=250, null=True)),
                ('diagnosis_1', models.CharField(blank=True, max_length=250, null=True)),
                ('diagnosis_2', models.CharField(blank=True, max_length=250, null=True)),
                ('department_surgery_0', models.CharField(blank=True, max_length=150, null=True)),
                ('department_surgery_1', models.CharField(blank=True, max_length=150, null=True)),
                ('department_surgery_2', models.CharField(blank=True, max_length=150, null=True)),
                ('income_date', models.DateField(blank=True, null=True)),
                ('surgery_date', models.DateField(blank=True, null=True)),
                ('exit_date', models.DateField(blank=True, null=True)),
                ('doctor_surgery_0', models.CharField(blank=True, max_length=150, null=True)),
                ('doctor_surgery_1', models.CharField(blank=True, max_length=150, null=True)),
                ('doctor_surgery_2', models.CharField(blank=True, max_length=150, null=True)),
                ('doctor_anestesia_0', models.CharField(blank=True, max_length=150, null=True)),
                ('doctor_anestesia_1', models.CharField(blank=True, max_length=150, null=True)),
                ('doctor_anestesia_2', models.CharField(blank=True, max_length=150, null=True)),
                ('nurse_0', models.CharField(blank=True, max_length=150, null=True)),
                ('nurse_1', models.CharField(blank=True, max_length=150, null=True)),
                ('nurse_2', models.CharField(blank=True, max_length=150, null=True)),
                ('medicine_description_0', models.CharField(blank=True, max_length=500, null=True)),
                ('medicine_description_1', models.CharField(blank=True, max_length=500, null=True)),
                ('medicine_description_2', models.CharField(blank=True, max_length=500, null=True)),
                ('price_man', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('price_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('additional_info_0', models.CharField(blank=True, max_length=250, null=True)),
                ('additional_info_1', models.CharField(blank=True, max_length=250, null=True)),
                ('additional_info_2', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hospital_surgery', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='surgery_hospital', to='dicts.hospital')),
                ('hospital_therapy', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='surgery_therapy_hospital', to='dicts.hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patients.patient')),
            ],
            options={
                'db_table': 'patient_surgery',
                'managed': True,
            },
        ),
    ]
