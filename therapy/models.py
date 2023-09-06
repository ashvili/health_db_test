from django.db import models

from health.utils import get_data_lang
from dicts.models import Doctor, Hospital
from patients.models import Patient


class PatientTherapy(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, to_field='id', related_name='therapy_patient')

    diagnosis_0 = models.TextField(blank=True, null=True)
    diagnosis_1 = models.TextField(blank=True, null=True)
    diagnosis_2 = models.TextField(blank=True, null=True)

    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, to_field='id',
                                 blank=True, null=True,
                                 related_name='therapy_hospital', default=None)

    hospital_therapy = models.ForeignKey(Hospital, on_delete=models.PROTECT, to_field='id',
                                         blank=True, null=True,
                                         related_name='hospital_therapy_hospital', default=None)
    department_therapy_0 = models.CharField(max_length=150, blank=True, null=True)
    department_therapy_1 = models.CharField(max_length=150, blank=True, null=True)
    department_therapy_2 = models.CharField(max_length=150, blank=True, null=True)

    income_date = models.DateField(blank=True, null=True)

    exit_date = models.DateField(blank=True, null=True)

    therapy_description_0 = models.TextField(blank=True, null=True)
    therapy_description_1 = models.TextField(blank=True, null=True)
    therapy_description_2 = models.TextField(blank=True, null=True)

    # doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, to_field='id', related_name='therapy_doctor', default=None)
    doctor_0 = models.CharField(max_length=150, blank=True, null=True)
    doctor_1 = models.CharField(max_length=150, blank=True, null=True)
    doctor_2 = models.CharField(max_length=150, blank=True, null=True)

    price_man = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    price_usd = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    additional_info_0 = models.TextField(blank=True, null=True)
    additional_info_1 = models.TextField(blank=True, null=True)
    additional_info_2 = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def diagnosis(self):
        if get_data_lang() == 'en':
            return self.diagnosis_0
        elif get_data_lang() == 'tk':
            return self.diagnosis_2
        else:
            return self.diagnosis_1
    @property
    def department_therapy(self):
        if get_data_lang() == 'en':
            return self.department_therapy_0
        elif get_data_lang() == 'tk':
            return self.department_therapy_2
        else:
            return self.department_therapy_1
    @property
    def therapy_description(self):
        if get_data_lang() == 'en':
            return self.therapy_description_0
        elif get_data_lang() == 'tk':
            return self.therapy_description_2
        else:
            return self.therapy_description_1
    @property
    def doctor(self):
        if get_data_lang() == 'en':
            return self.doctor_0
        elif get_data_lang() == 'tk':
            return self.doctor_2
        else:
            return self.doctor_1
    @property
    def additional_info(self):
        if get_data_lang() == 'en':
            return self.additional_info_0
        elif get_data_lang() == 'tk':
            return self.additional_info_2
        else:
            return self.additional_info_1

    class Meta:
        managed = True
        db_table = 'patient_therapy'
        verbose_name_plural = 'Записи о лечении'
        verbose_name = 'Лечение'
        ordering = ['-created_at',]
