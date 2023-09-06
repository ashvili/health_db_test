from django.db import models

from health.utils import get_data_lang
from dicts.models import Hospital
from patients.models import Patient


class PatientDiagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, to_field='id', related_name='diagnosis_patient')

    diagnosis_0 = models.TextField(blank=True, null=True)
    diagnosis_1 = models.TextField(blank=True, null=True)
    diagnosis_2 = models.TextField(blank=True, null=True)

    diagnosis_description_0 = models.TextField(blank=True, null=True)
    diagnosis_description_1 = models.TextField(blank=True, null=True)
    diagnosis_description_2 = models.TextField(blank=True, null=True)

    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, to_field='id', related_name='diagnosis_hospital', default=None)

    income_date = models.DateField(blank=True, null=True)
    diagnosis_date = models.DateField(blank=True, null=True)
    exit_date = models.DateField(blank=True, null=True)

    doctor_diagnosis_0 = models.CharField(max_length=150, blank=True, null=True)
    doctor_diagnosis_1 = models.CharField(max_length=150, blank=True, null=True)
    doctor_diagnosis_2 = models.CharField(max_length=150, blank=True, null=True)

    price_man = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    price_usd = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    additional_info_0 = models.CharField(max_length=250, blank=True, null=True)
    additional_info_1 = models.CharField(max_length=250, blank=True, null=True)
    additional_info_2 = models.CharField(max_length=250, blank=True, null=True)

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
    def doctor_diagnosis(self):
        if get_data_lang() == 'en':
            return self.doctor_diagnosis_0
        elif get_data_lang() == 'tk':
            return self.doctor_diagnosis_2
        else:
            return self.doctor_diagnosis_1
    @property
    def diagnosis_description(self):
        if get_data_lang() == 'en':
            return self.diagnosis_description_0
        elif get_data_lang() == 'tk':
            return self.diagnosis_description_2
        else:
            return self.diagnosis_description_1
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
        db_table = 'patient_diagnosis'
        verbose_name_plural = 'Записи диагностики'
        verbose_name = 'Диагноз'
        ordering = ['-created_at',]
