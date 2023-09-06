import datetime

from django import forms
from django.db.models import Q, F
from django.utils.translation import gettext_lazy as _

from crispy_forms.bootstrap import FormActions, TabHolder, Tab, InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Fieldset, MultiField, Div, Field
from easy_select2 import Select2

from health import settings
from patients.models import Patient
from .models import PatientResolution
from dicts.models import Sex


class PatientResolutionForm(forms.ModelForm):
    id = forms.IntegerField(disabled=True, required=False)
    # patient = forms.ModelChoiceField(
    #     queryset=Patient.objects.filter(Q(resolution_patient_patient__isnull=True) |
    #                                     Q(resolution_patient_patient=1 )),
    #     initial=None, required=False, label='Пациент',
    #     widget=Select2(select2attrs={'width': '100%'}))
    patient = forms.ModelChoiceField(queryset=Patient.objects.none(), initial=None, required=False, label=_('Пациент'),
                                     widget=Select2(select2attrs={'width': '100%', }))

    lastname_0 = forms.CharField(required=False, label=_('Фамилия'), widget=forms.TextInput())
    lastname_1 = forms.CharField(required=False, label=_('Фамилия'), widget=forms.TextInput())
    lastname_2 = forms.CharField(required=False, label=_('Фамилия'), widget=forms.TextInput())

    date_birthday = forms.DateField(
                                    widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                    required=False, label=_('Дата рождения'),
                                   )

    sex = forms.ModelChoiceField(queryset=Sex.objects.all(), initial=None, required=False, label=_('Пол'),
                                 empty_label='')

    income_date = forms.DateField(
                                    widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                    required=False, label=_('Дата поступления'),
                                   )

    resolution_name_0 = forms.CharField(required=False, label=_('Имя по решению'), widget=forms.TextInput())
    resolution_name_1 = forms.CharField(required=False, label=_('Имя по решению'), widget=forms.TextInput())
    resolution_name_2 = forms.CharField(required=False, label=_('Имя по решению'), widget=forms.TextInput())

    resolution_number = forms.CharField(required=False, label=_('Номер решения'), widget=forms.TextInput())
    resolution_date = forms.DateField(
                                    widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                    required=False, label=_('Дата решения'),
                                   )
    birth_certificate_date = forms.DateField(
                                    widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                    required=False, label=_('Дата свид. о рожд.'),
                                   )

    class Meta:
        model = PatientResolution
        fields = [
            'id', 'patient',
            'lastname_0', 'lastname_1', 'lastname_2',
            'date_birthday', 'sex', 'income_date',
            'resolution_name_0', 'resolution_name_1', 'resolution_name_2',
            'resolution_number', 'resolution_date',
            'birth_certificate_date'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['patient'].disabled = not (self.instance.patient is None)
        self.fields['patient'].queryset = Patient.objects.filter(
            Q(resolution_patient_patient__isnull=True) |
            Q(resolution_patient_patient=self.instance.pk))

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                TabHolder(
                    Tab(_('Туркменский'),
                        'lastname_2',
                        Div(
                            Div('date_birthday', css_class='col-4', ),
                            Div('sex', css_class='col-4', ),
                        css_class='row'),
                        Div(
                            Div('income_date', css_class='col-4', ),
                        css_class='row'),
                        'resolution_name_2',
                        Div(
                            Div('resolution_number', css_class='col-4', ),
                            Div('resolution_date', css_class='col-4', ),
                        css_class='row'),
                        Div(
                            Div('birth_certificate_date', css_class='col-4', ),
                        css_class='row'),
                        Div(
                            Div('patient', css_class='col-12', ),
                        css_class='row'),
                    ),
                    Tab(_('Русский'),
                        'lastname_1',
                        'resolution_name_1',
                        ),
                    # Tab(_('Английский'),
                    #     'lastname_0',
                    #     'resolution_name_0',
                    #     ),
                ),
                FormActions(
                    Submit('save', _('Сохранить')),
                    Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary"),
                ),
                css_class='form card col-8',
            ),
        )

class PatientResolutionSearchForm(forms.Form):
    YEARS = [(None, _('Год рождения')), ] + [(y, str(y)) for y in range(2000, datetime.date.today().year + 1)]

    fullname = forms.CharField(required=False, label='', #_('Имя Фамилия'),
                               widget=forms.TextInput(attrs={'placeholder': _('Имя Фамилия ребенка'), })
                               )
    year_birthday = forms.ChoiceField(
        choices=YEARS,
        required=False,
        label='', #_('Год рождения'),
        initial=_('Год рождения'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('fullname', css_class='col-6 align-self-end', ),
                    Div('year_birthday', css_class='col-3 align-self-end', ),
                    Div(
                        FormActions(
                            Submit('search', _('Найти')),
                        ),
                        css_class='col-2 align-self-end',
                    ),
                    css_class='row'),
                css_class='',
            ),
        )
