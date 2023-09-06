from django.db import models

from dicts.models import Unit
from health.utils import get_data_lang


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name_0 = models.CharField(max_length=150, blank=True, null=True)
    name_1 = models.CharField(max_length=150, blank=True, null=True)
    name_2 = models.CharField(max_length=150, blank=True, null=True)
    source = models.BooleanField(default=False)
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
        db_table = 'organizarion'
        verbose_name_plural = 'Организации'
        verbose_name = 'Организация'
        ordering = ['name_0',]

class Investment(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.ForeignKey(Organization, on_delete=models.PROTECT, to_field='id',
                               related_name='source_investment_organization', default=None)

    destination_0 = models.CharField(max_length=150, blank=True, null=True)
    destination_1 = models.CharField(max_length=150, blank=True, null=True)
    destination_2 = models.CharField(max_length=150, blank=True, null=True)

    child_count = models.IntegerField()

    investment_date = models.DateField(blank=True, null=True)

    investment_name_0 = models.CharField(max_length=150, blank=True, null=True)
    investment_name_1 = models.CharField(max_length=150, blank=True, null=True)
    investment_name_2 = models.CharField(max_length=150, blank=True, null=True)

    count = models.DecimalField(max_digits=19, decimal_places=2)
    price_man = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    price_usd = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    investor = models.ForeignKey(Organization, on_delete=models.PROTECT, to_field='id',
                               related_name='investor_investment_organization', default=None, blank=True, null=True)

    investor_0 = models.CharField(max_length=150, blank=True, null=True)
    investor_1 = models.CharField(max_length=150, blank=True, null=True)
    investor_2 = models.CharField(max_length=150, blank=True, null=True)

    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, to_field='id',
                               related_name='investment_unit', default=None)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def destination(self):
        if get_data_lang() == 'en':
            return self.destination_0
        elif get_data_lang() == 'tk':
            return self.destination_2
        else:
            return self.destination_1
    @property
    def investment_name(self):
        if get_data_lang() == 'en':
            return self.investment_name_0
        elif get_data_lang() == 'tk':
            return self.investment_name_2
        else:
            return self.investment_name_1

    class Meta:
        managed = True
        db_table = 'investment'
        verbose_name_plural = 'Использование средств'
        verbose_name = 'Использование средств'
        ordering = ['-created_at',]
