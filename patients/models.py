from django.db import models

from health.utils import get_data_lang
from dicts.models import City, Education_institution, Sex, Etrap


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    fullname_0 = models.CharField(max_length=150, blank=True, null=True)
    fullname_1 = models.CharField(max_length=150, blank=True, null=True)
    fullname_2 = models.CharField(max_length=150, blank=True, null=True)

    comment_0 = models.CharField(max_length=250, blank=True, null=True)
    comment_1 = models.CharField(max_length=250, blank=True, null=True)
    comment_2 = models.CharField(max_length=250, blank=True, null=True)

    address_0 = models.CharField(max_length=250, blank=True, null=True)
    address_1 = models.CharField(max_length=250, blank=True, null=True)
    address_2 = models.CharField(max_length=250, blank=True, null=True)

    etrap = models.ForeignKey(Etrap, on_delete=models.PROTECT, to_field='id', related_name='relation_patient_etrap',
                              default=None, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, to_field='id', related_name='relation_patient_city',
                             default=None, null=True)

    sex = models.ForeignKey(Sex, on_delete=models.PROTECT, to_field='id', default=None, null=True)
    education_institution = models.ForeignKey(Education_institution, on_delete=models.PROTECT, to_field='id',
                                              default=None, null=True)

    date_birthday = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'patient'
        verbose_name_plural = 'Пациенты'
        verbose_name = 'Пациент'
        ordering = ['-created_at',]

    def __str__(self):
        return f'{self.fullname}., {self.date_birthday}'

    @property
    def fullname(self):
        if get_data_lang() == 'en':
            return self.fullname_0
        elif get_data_lang() == 'tk':
            return self.fullname_2
        else:
            return self.fullname_1

    @property
    def address(self):
        if get_data_lang() == 'en':
            return self.address_0
        elif get_data_lang() == 'tk':
            return self.address_2
        else:
            return self.address_1

    @property
    def comment(self):
        if get_data_lang() == 'en':
            return self.comment_0
        elif get_data_lang() == 'tk':
            return self.comment_2
        else:
            return self.comment_1

