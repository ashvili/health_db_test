from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.bootstrap import FormActions, TabHolder, Tab, InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, Div, Field, Hidden
from easy_select2 import Select2

from dicts.models import Unit
from health import settings
from investment.models import Investment, Organization


class InvestmentForm(forms.ModelForm):
    destination_0 = forms.CharField(required=False, label=_('Куда направляется помощь'), widget=forms.TextInput())
    destination_1 = forms.CharField(required=False, label=_('Куда направляется помощь'), widget=forms.TextInput())
    destination_2 = forms.CharField(required=True, label=_('Куда направляется помощь'), widget=forms.TextInput())

    investment_name_0 = forms.CharField(required=False, label=_('Наименование товара / услуги'), widget=forms.TextInput())
    investment_name_1 = forms.CharField(required=False, label=_('Наименование товара / услуги'), widget=forms.TextInput())
    investment_name_2 = forms.CharField(required=True, label=_('Наименование товара / услуги'), widget=forms.TextInput())

    child_count = forms.IntegerField(required=False, label=_('Кол-во детей'), widget=forms.NumberInput())

    count = forms.DecimalField(max_digits=19, decimal_places=2,
                               label='Кол-во',
                               required=True,
                               widget=forms.NumberInput())

    price_man = forms.DecimalField(max_digits=19, decimal_places=2,
                                   label=_('Стоимость'),
                                   required=True,
                                   widget=forms.NumberInput())

    source = forms.ModelChoiceField(queryset=Organization.objects.filter(source=True),
                                    required=True,
                                    initial=None,
                                    label=_('Источник'),
                                    widget=Select2(select2attrs={'width': '100%'}),
                                    )
    # investor = forms.ModelChoiceField(queryset=Organization.objects.filter(source=False),
    #                                   required=True,
    #                                   initial=None,
    #                                   label='Поставщик',
    #                                   widget=forms.Select(),
    #                                 )
    investor_0 = forms.CharField(required=False, label=_('Поставщик'), widget=forms.TextInput())
    investor_1 = forms.CharField(required=False, label=_('Поставщик'), widget=forms.TextInput())
    investor_2 = forms.CharField(required=True, label=_('Поставщик'), widget=forms.TextInput())

    investment_date = forms.DateField(
                                  widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                  required=True,
                                  label=_('Дата'),
                                  )
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(),
                                  required=False,
                                  initial=None,
                                  label=_('Ед. измерения'),
                                  widget=Select2(select2attrs={'width': '100%'}),
                                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                TabHolder(
                    Tab(_('Туркменский'),
                        Div(
                            Div('destination_2', css_class='col-8',),
                            Div('child_count', css_class='col-4',),
                        css_class='row',
                        ),
                        Div(
                            Div('investment_name_2', css_class='col-6',),
                            Div('count', css_class='col-3',),
                            Div('unit', css_class='col-3',),
                        css_class='row',
                        ),
                        Div(
                            Div('source', css_class='col-5',),
                            Div('investor_2', css_class='col-7',),
                        css_class='row',
                        ),
                        Div(
                            Div('price_man', css_class='col-6',),
                            Div('investment_date', css_class='col-6',),
                        css_class='row',
                        ),
                    ),
                    Tab(_('Русский'),
                        Div(
                            Div('destination_1', css_class='col-8', ),
                        ),
                        Div(
                            Div('investment_name_1', css_class='col-8', ),
                        ),
                        Div(
                            Div('investor_1', css_class='col-8', ),
                        ),
                    ),
                    # Tab(_('Английский'),
                    #     Div(
                    #         Div('destination_0', css_class='col-8', ),
                    #     ),
                    #     Div(
                    #         Div('investment_name_0', css_class='col-8', ),
                    #     ),
                    #     Div(
                    #         Div('investor_0', css_class='col-8', ),
                    #     ),
                    # ),
                ),
                FormActions(
                    Submit('save', _('Сохранить')),
                    # Button('delete', 'Удалить',
                    #        onclick='window.location.href = "{}";'.format(
                    #            reverse('dicts:city_delete', kwargs={'pk': self.instance.pk})),
                    #        css_class ="btn btn-danger"
                    #        ) if self.instance.pk else HTML(''),
                    Button('cancel', _('Назад'), onclick='history.back()', css_class="btn btn-secondary")
                ),
            css_class='form card col-8',
            ),
        )

    class Meta:
        model = Investment
        fields = [
            'id', 'source', 'investor',
            'destination_0', 'destination_1', 'destination_2',
            'child_count', 'investment_date',
            'investment_name_0', 'investment_name_1', 'investment_name_2',
            'count', 'price_man', 'unit',
            'investor_0', 'investor_1', 'investor_2',
        ]

class InvestmentSearchForm(forms.Form):
    fullname = forms.CharField(required=False, label=_('Поставщик'),
                               widget=forms.TextInput(attrs={'placeholder': _('Поставщик'), })
                               )
    date_start = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False, label=_('Начало'),
        input_formats=['%d%m%Y'],
        localize=False,
    )
    date_end = forms.DateField(
        widget=forms.NumberInput(attrs={'type': 'date', 'format': '%d-%m-%Y'}),
        required=False, label=_('Конец'),
        localize=False,
    )
    date_period = forms.ChoiceField(choices=settings.PERIODS,
                                    required=False,
                                    label=_('Период (дата поступления)'),
                                    widget=forms.Select(attrs={'onchange': 'setDates()'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('fullname', css_class='col-6', ),
                    ),
                Div(
                    Div('date_period', css_class='col-4 align-self-end', ),
                    Div('date_start', css_class='col-3 align-self-end', ),
                    Div('date_end', css_class='col-3 align-self-end', ),
                    Div(
                        FormActions(
                            Submit('search', _('Найти')),
                        ),
                        css_class='col-2 align-self-end',
                    ),
                    css_class='row'),
                css_class='card card-body',
            ),
        )
