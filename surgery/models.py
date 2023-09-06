from django.db import models

from health.utils import get_data_lang
from dicts.models import Hospital, SurgeryType
from patients.models import Patient


class PatientSurgery(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, to_field='id', related_name='surgery_patient_patient')

    diagnosis_0 = models.TextField(blank=True, null=True)
    diagnosis_1 = models.TextField(blank=True, null=True)
    diagnosis_2 = models.TextField(blank=True, null=True)

    surgery_type = models.ForeignKey(SurgeryType, on_delete=models.PROTECT,
                                     blank=True, null=True,
                                     to_field='id', related_name='surgery_patient_surgery_type')

    hospital_therapy = models.ForeignKey(Hospital, on_delete=models.PROTECT, to_field='id', related_name='surgery_therapy_hospital', default=None)
    hospital_surgery = models.ForeignKey(Hospital, on_delete=models.PROTECT, to_field='id', related_name='surgery_hospital', default=None)

    department_surgery_0 = models.CharField(max_length=150, blank=True, null=True)
    department_surgery_1 = models.CharField(max_length=150, blank=True, null=True)
    department_surgery_2 = models.CharField(max_length=150, blank=True, null=True)

    income_date = models.DateField(blank=True, null=True)
    surgery_date = models.DateField(blank=True, null=True)
    exit_date = models.DateField(blank=True, null=True)

    doctor_surgery_0 = models.CharField(max_length=150, blank=True, null=True) # хирурн
    doctor_surgery_1 = models.CharField(max_length=150, blank=True, null=True)
    doctor_surgery_2 = models.CharField(max_length=150, blank=True, null=True)

    doctor_anestesia_0 = models.CharField(max_length=150, blank=True, null=True) # анестезиолог
    doctor_anestesia_1 = models.CharField(max_length=150, blank=True, null=True)
    doctor_anestesia_2 = models.CharField(max_length=150, blank=True, null=True)

    nurse_0 = models.CharField(max_length=150, blank=True, null=True) # медсестра
    nurse_1 = models.CharField(max_length=150, blank=True, null=True) # медсестра
    nurse_2 = models.CharField(max_length=150, blank=True, null=True) # медсестра

    medicine_description_0 = models.TextField(blank=True, null=True)
    medicine_description_1 = models.TextField(blank=True, null=True)
    medicine_description_2 = models.TextField(blank=True, null=True)

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
    def departament_surgery(self):
        if get_data_lang() == 'en':
            return self.departament_surgery_0
        elif get_data_lang() == 'tk':
            return self.departament_surgery_2
        else:
            return self.departament_surgery_1
    @property
    def doctor_surgery(self):
        if get_data_lang() == 'en':
            return self.doctor_surgery_0
        elif get_data_lang() == 'tk':
            return self.doctor_surgery_2
        else:
            return self.doctor_surgery_1
    @property
    def doctor_anestesia(self):
        if get_data_lang() == 'en':
            return self.doctor_anestesia_0
        elif get_data_lang() == 'tk':
            return self.doctor_anestesia_2
        else:
            return self.doctor_anestesia_1
    @property
    def nurse(self):
        if get_data_lang() == 'en':
            return self.nurse_0
        elif get_data_lang() == 'tk':
            return self.nurse_2
        else:
            return self.nurse_1
    @property
    def medicine_description(self):
        if get_data_lang() == 'en':
            return self.medicine_description_0
        elif get_data_lang() == 'tk':
            return self.medicine_description_2
        else:
            return self.medicine_description_1
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
        db_table = 'patient_surgery'
        verbose_name_plural = 'Операции'
        verbose_name = 'Операция'
        ordering = ['-created_at',]
