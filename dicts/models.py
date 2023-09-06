from django.db import models
from django_currentuser.middleware import get_current_authenticated_user

from health.utils import get_data_lang


class Etrap(models.Model):
    id = models.AutoField(primary_key=True)
    name_0 = models.CharField(max_length=50, blank=True, null=True)
    name_1 = models.CharField(max_length=50, blank=True, null=True)
    name_2 = models.CharField(max_length=50, blank=True, null=True)

    @property
    def name(self):
        if get_data_lang() == 'en':
            return self.name_0
        elif get_data_lang() == 'tk':
            return self.name_2
        else:
            return self.name_1
    def __str__(self):
        return f'{self.name}'
    class Meta:
        managed = True
        db_table = 'etrap'
        verbose_name_plural = 'Велаяты/города'
        verbose_name = 'Велаят/город'
        ordering = ['name_0',]


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name_0 = models.CharField(max_length=50, blank=True, null=True)
    name_1 = models.CharField(max_length=50, blank=True, null=True)
    name_2 = models.CharField(max_length=50, blank=True, null=True)
    etrap = models.ForeignKey(Etrap, on_delete=models.PROTECT, to_field='id')

    @property
    def name(self):
        if get_data_lang() == 'en':
            return self.name_0
        elif get_data_lang() == 'tk':
            return self.name_2
        else:
            return self.name_1
    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = True
        db_table = 'city'
        ordering = ['etrap', 'name_0']
        verbose_name_plural = 'Города/этрапы'
        verbose_name = 'Город/этрап'


class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    name_0 = models.CharField(max_length=50, blank=True, null=True)
    name_1 = models.CharField(max_length=50, blank=True, null=True)
    name_2 = models.CharField(max_length=50, blank=True, null=True)

    @property
    def name(self):
        if get_data_lang() == 'en':
            return self.name_0
        elif get_data_lang() == 'tk':
            return self.name_2
        else:
            return self.name_1
    def __str__(self):
        return f'{self.name}'
    class Meta:
        managed = True
        db_table = 'sex'
        verbose_name_plural = 'Пол'
        verbose_name = 'Пол'


class Education_institution(models.Model):
    id = models.AutoField(primary_key=True)
    name_0 = models.CharField(max_length=250, blank=True, null=True)
    name_1 = models.CharField(max_length=250, blank=True, null=True)
    name_2 = models.CharField(max_length=250, blank=True, null=True)
    address_0 = models.CharField(max_length=250, blank=True, null=True)
    address_1 = models.CharField(max_length=250, blank=True, null=True)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    etrap = models.ForeignKey(Etrap, on_delete=models.PROTECT, to_field='id',
                              blank=True, null=True,
                              related_name='relation_education_institution_etrap')
    city = models.ForeignKey(City, on_delete=models.PROTECT, to_field='id', related_name='relation_education_institution_city')

    @property
    def name(self):
        if get_data_lang() == 'en':
            return self.name_0
        elif get_data_lang() == 'tk':
            return self.name_2
        else:
            return self.name_1
    @property
    def address(self):
        if get_data_lang() == 'en':
            return self.address_0
        elif get_data_lang() == 'tk':
            return self.address_2
        else:
            return self.address_1

    class Meta:
        managed = True
        db_table = 'education_institution'
        verbose_name_plural = 'Учебные заведения'
        verbose_name = 'Учебное заведение'
        ordering = ['name_0',]

    def __str__(self):
        return f'{self.name}, {self.city}'


class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name_0 = models.CharField(max_length=250, blank=True, null=True)
    name_1 = models.CharField(max_length=250, blank=True, null=True)
    name_2 = models.CharField(max_length=250, blank=True, null=True)
    address_0 = models.CharField(max_length=250, blank=True, null=True)
    address_1 = models.CharField(max_length=250, blank=True, null=True)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    etrap = models.ForeignKey(Etrap, on_delete=models.PROTECT, to_field='id',
                              blank=True, null=True,
                              related_name='relation_hospital_etrap')
    city = models.ForeignKey(City, on_delete=models.PROTECT, to_field='id', related_name='relation_hospital_city')

    @property
    def name(self):
        if get_data_lang() == 'en':
            return self.name_0
        elif get_data_lang() == 'tk':
            return self.name_2
        else:
            return self.name_1
    @property
    def address(self):
        if get_data_lang() == 'en':
            return self.address_0
        elif get_data_lang() == 'tk':
            return self.address_2
        else:
            return self.address_1
    def __str__(self):
        return f'{self.name}, {self.city}'

    class Meta:
        managed = True
        db_table = 'hospital'
        verbose_name_plural = 'Больницы'
        verbose_name = 'Больница'
        ordering = ['name_0',]


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    fullname_0 = models.CharField(max_length=150, blank=True, null=True)
    fullname_1 = models.CharField(max_length=150, blank=True, null=True)
    fullname_2 = models.CharField(max_length=150, blank=True, null=True)
    date_birthday = models.DateField(blank=True, null=True)

    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, to_field='id')

    sex = models.ForeignKey(Sex, on_delete=models.PROTECT, to_field='id')

    class Meta:
        managed = True
        db_table = 'doctor'
        ordering = ['fullname_0']
        verbose_name_plural = 'Врачи'
        verbose_name = 'Врач'

    def __str__(self):
        return f'{self.fullname}'

    @property
    def fullname(self):
        if get_data_lang() == 'en':
            return self.fullname_0
        elif get_data_lang() == 'tk':
            return self.fullname_2
        else:
            return self.fullname_1


class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name_0 = models.CharField(max_length=150, blank=True, null=True)
    name_1 = models.CharField(max_length=150, blank=True, null=True)
    name_2 = models.CharField(max_length=150, blank=True, null=True)

    @property
    def name(self):
        if get_data_lang() == 'en':
            return self.name_0
        elif get_data_lang() == 'tk':
            return self.name_2
        else:
            return self.name_1
    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = True
        db_table = 'unit'
        verbose_name_plural = 'Ед. измерения'
        verbose_name = 'Ед. измерения'
        ordering = ['name_0',]


class SurgeryType(models.Model):
    id = models.AutoField(primary_key=True)
    name_0 = models.CharField(max_length=50, blank=True, null=True)
    name_1 = models.CharField(max_length=50, blank=True, null=True)
    name_2 = models.CharField(max_length=50, blank=True, null=True)

    @property
    def name(self):
        if get_data_lang() == 'en':
            return self.name_0
        elif get_data_lang() == 'tk':
            return self.name_2
        else:
            return self.name_1
    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = True
        db_table = 'surgery_type'
        verbose_name_plural = 'Тип операции'
        verbose_name = 'Типы операций'
        ordering = ['name_0',]

