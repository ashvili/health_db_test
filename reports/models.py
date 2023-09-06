from django.db import models
from django.urls import reverse_lazy

from dicts.models import Hospital
from health.utils import get_data_lang


class ReportByVelayatModel(models.Model):
    etrap_id = models.IntegerField(primary_key=True) #, blank=True, null=True)
    etrap_name_0 = models.CharField(max_length=50, blank=True, null=True)
    etrap_name_1 = models.CharField(max_length=50, blank=True, null=True)
    etrap_name_2 = models.CharField(max_length=50, blank=True, null=True)

    surgery_count = models.IntegerField(blank=True, null=True)
    surgery_sum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    therapy_count = models.IntegerField(blank=True, null=True)
    therapy_sum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    diagnosis_count = models.IntegerField(blank=True, null=True)
    diagnosis_sum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    total_count = models.IntegerField(blank=True, null=True)
    total_sum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    @property
    def etrap_name(self):
        if get_data_lang() == 'en':
            return self.etrap_name_0
        elif get_data_lang() == 'tk':
            return self.etrap_name_2
        else:
            return self.etrap_name_1
    class Meta:
        managed = False


class PatientEvent(models.Model):
    original_id = models.IntegerField()
    id = models.CharField(primary_key=True ,max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    description_0 = models.CharField(max_length=250, blank=True, null=True)
    description_1 = models.CharField(max_length=250, blank=True, null=True)
    description_2 = models.CharField(max_length=250, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_type = models.SmallIntegerField()
    price_man = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    # hospital_id = models.ForeignKey
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, to_field='id', default=None)

    event_names_0 = ('Surgery', 'Therapy', 'Diagnosis', 'Resolution')
    event_names_1 = ('Операция', 'Терапия', 'Диагностика', 'Решение')
    event_names_2 = ('Operasiýa', 'Bejergi', 'Keseliň kesgidi', 'Çözgüt')
    @property
    def event_name(self):
        if get_data_lang() == 'en':
            return self.event_names_0[self.event_type]
        elif get_data_lang() == 'tk':
            return self.event_names_2[self.event_type]
        else:
            return self.event_names_1[self.event_type]

    @property
    def description(self):
        if get_data_lang() == 'en':
            return self.description_0
        elif get_data_lang() == 'tk':
            return self.description_2
        else:
            return self.description_1

    @property
    def link(self):
        if self.event_type == 0:
            result = reverse_lazy('surgery:surgery_edit', kwargs={'pk': self.original_id, })
        elif self.event_type == 1:
            result = reverse_lazy('therapy:therapy_edit', kwargs={'pk': self.original_id, })
        elif self.event_type == 2:
            result = reverse_lazy('diagnosis:diagnosis_edit', kwargs={'pk': self.original_id, })
        elif self.event_type == 3:
            result = reverse_lazy('resolutions:resolution_edit', kwargs={'pk': self.original_id, })
        return result
    class Meta:
        managed = False
        db_table = 'v_patient_event'

class ReportByMonthModel(models.Model):
    id = models.IntegerField(primary_key=True)
    month_name = models.CharField(max_length=20) #, blank=True, null=True)

    surgery_count = models.IntegerField(blank=True, null=True)
    surgery_sum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    therapy_count = models.IntegerField(blank=True, null=True)
    therapy_sum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    diagnosis_count = models.IntegerField(blank=True, null=True)
    diagnosis_sum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    total_count = models.IntegerField(blank=True, null=True)
    total_sum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    @property
    def month(self):
        if (isinstance(self.month_name, str) and len(self.month_name) > 0):
            res = self.month_name.split('-')
            return f'{res[1]}.{res[0]}'
        return ''
    class Meta:
        managed = False