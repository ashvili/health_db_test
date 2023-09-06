from django.db import models

from dicts.models import Sex
from health.utils import get_data_lang
from patients.models import Patient


class PatientResolution(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient,
                                on_delete=models.PROTECT,
                                to_field='id',
                                default=None,
                                null=True,
                                related_name='resolution_patient_patient')

    lastname_0 = models.CharField(max_length=150, blank=True, null=True)
    lastname_1 = models.CharField(max_length=150, blank=True, null=True)
    lastname_2 = models.CharField(max_length=150, blank=True, null=True)

    date_birthday = models.DateField(blank=True, null=True)

    sex = models.ForeignKey(Sex, on_delete=models.PROTECT, to_field='id', default=None, null=True, related_name='resolution_patient_sex')

    income_date = models.DateField(blank=True, null=True)

    resolution_name_0 = models.CharField(max_length=150, blank=True, null=True)
    resolution_name_1 = models.CharField(max_length=150, blank=True, null=True)
    resolution_name_2 = models.CharField(max_length=150, blank=True, null=True)

    resolution_number = models.CharField(max_length=50, blank=True, null=True)
    resolution_date = models.DateField(blank=True, null=True)
    birth_certificate_date = models.DateField(blank=True, null=True)

    additional_info_0 = models.CharField(max_length=250, blank=True, null=True)
    additional_info_1 = models.CharField(max_length=250, blank=True, null=True)
    additional_info_2 = models.CharField(max_length=250, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def lastname(self):
        if get_data_lang() == 'en':
            return self.lastname_0
        elif get_data_lang() == 'tk':
            return self.lastname_2
        else:
            return self.lastname_1
    @property
    def resolution_name(self):
        if get_data_lang() == 'en':
            return self.resolution_name_0
        elif get_data_lang() == 'tk':
            return self.resolution_name_2
        else:
            return self.resolution_name_1
    @property
    def additional_info(self):
        if get_data_lang() == 'en':
            return self.additional_info_0
        elif get_data_lang() == 'tk':
            return self.additional_info_2
        else:
            return self.additional_info_1

    def __str__(self):
        return f'{self.lastname} {self.resolution_name}, {self.date_birthday}'

    class Meta:
        managed = True
        db_table = 'patient_resolution'
        verbose_name_plural = 'Решения'
        verbose_name = 'Решение'
        ordering = ['-created_at',]

