from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.bootstrap import FormActions, TabHolder, Tab, InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, Div, Field, Hidden
from easy_select2 import Select2

from health import settings
from patients.models import Patient
from dicts.models import Hospital, SurgeryType
from .models import PatientSurgery


class SurgeryPatientEditForm(forms.ModelForm):
    diagnosis_0 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, }))
    diagnosis_1 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, }))
    diagnosis_2 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, }))

    surgery_type = forms.ModelChoiceField(queryset=SurgeryType.objects.all(),
                                              required=False,
                                              initial=None,
                                              label=_('Тип операции'),
                                              widget=Select2(select2attrs={'width': '100%'}),
                                              )

    hospital_therapy = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                              required=True,
                                              initial=None,
                                              label=_('Больница, проводящая лечение'),
                                              widget=Select2(select2attrs={'width': '100%'}),
                                              )
    hospital_surgery = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                              required=True,
                                              initial=None,
                                              label=_('Больница, где проводится операция'),
                                              widget=Select2(select2attrs={'width': '100%'}),
                                              )
    department_surgery_0 = forms.CharField(required=False, label=_('Отделение'), widget=forms.Textarea(attrs={'rows':3, }))
    department_surgery_1 = forms.CharField(required=False, label=_('Отделение'), widget=forms.Textarea(attrs={'rows':3, }))
    department_surgery_2 = forms.CharField(required=False, label=_('Отделение'), widget=forms.Textarea(attrs={'rows':3, }))

    income_date = forms.DateField(
                                  widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                  required=False,
                                  label=_('Дата госпитализации'),
                                  )
    surgery_date = forms.DateField(
                                widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                required=False,
                                label=_('Дата операции'),
                                )
    exit_date = forms.DateField(
                                widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                required=False,
                                label=_('Дата выписки'),
                                )

    doctor_surgery_0 = forms.CharField(required=False,
                                            label=_('Оперировавший врач'),
                                            widget=forms.TextInput())
    doctor_surgery_1 = forms.CharField(required=False,
                                            label=_('Оперировавший врач'),
                                            widget=forms.TextInput())
    doctor_surgery_2 = forms.CharField(required=False,
                                            label=_('Оперировавший врач'),
                                            widget=forms.TextInput())
    doctor_anestesia_0 = forms.CharField(required=False,
                                            label='Анестезиолог',
                                            widget=forms.TextInput())
    doctor_anestesia_1 = forms.CharField(required=False,
                                            label=_('Анестезиолог'),
                                            widget=forms.TextInput())
    doctor_anestesia_2 = forms.CharField(required=False,
                                            label=_('Анестезиолог'),
                                            widget=forms.TextInput())
    nurse_0 = forms.CharField(required=False,
                                            label=_('Медсестра'),
                                            widget=forms.TextInput())
    nurse_1 = forms.CharField(required=False,
                                            label=_('Медсестра'),
                                            widget=forms.TextInput())
    nurse_2 = forms.CharField(required=False,
                                            label=_('Медсестра'),
                                            widget=forms.TextInput())

    medicine_description_0 = forms.CharField(required=False,
                                            label=_('Используемые медикаменты'),
                                            widget=forms.Textarea(attrs={'rows':3, }))
    medicine_description_1 = forms.CharField(required=False,
                                            label=_('Используемые медикаменты'),
                                            widget=forms.Textarea(attrs={'rows':3, }))
    medicine_description_2 = forms.CharField(required=False,
                                            label=_('Используемые медикаменты'),
                                            widget=forms.Textarea(attrs={'rows':3, }))

    price_man = forms.DecimalField(max_digits=19, decimal_places=2,
                                   label=_('Стоимость'),
                                   required=False,
                                   widget=forms.NumberInput())

    class Meta:
        model = PatientSurgery
        fields = [
            'id', 'patient', 'surgery_type',
            'diagnosis_0', 'diagnosis_1', 'diagnosis_2',
            'hospital_therapy', 'hospital_surgery',
            'department_surgery_0', 'department_surgery_1', 'department_surgery_2',
            'income_date', 'surgery_date', 'exit_date',
            'doctor_surgery_0', 'doctor_surgery_1', 'doctor_surgery_2',
            'doctor_anestesia_0', 'doctor_anestesia_1', 'doctor_anestesia_2',
            'nurse_0', 'nurse_1', 'nurse_2',
            'medicine_description_0', 'medicine_description_1', 'medicine_description_2',
            'price_man',
            'additional_info_0', 'additional_info_1', 'additional_info_2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                TabHolder(
                    Tab(_('Туркменский'),
                        Div('surgery_type', css_class='col-6',),
                        Div('diagnosis_2', css_class='col-12',),
                        Div(
                            Div('hospital_therapy', css_class='col-8', ),
                            Div('income_date', css_class='col-4', ),
                            css_class='row',
                        ),
                        Div(
                            Div('hospital_surgery', css_class='col-6', ),
                            Div('department_surgery_2', css_class='col-6', ),
                            css_class='row'
                        ),
                        Div(
                            Div('doctor_surgery_2', css_class='col-6', ),
                            Div('surgery_date', css_class='col-3', ),
                            Div('exit_date', css_class='col-3', ),
                            css_class='row'
                        ),
                        Div(
                            Div('doctor_anestesia_2', css_class='col-6', ),
                            Div('nurse_2', css_class='col-6', ),
                            css_class='row'
                        ),
                        'medicine_description_2',
                        Div('price_man', css_class='col-4', ),
                    ),
                    Tab(_('Русский'),
                        Div('diagnosis_1', css_class='col-12',),
                        Div('department_surgery_1', css_class='col-12', ),
                        Div(
                            Div('doctor_surgery_1', css_class='col-4', ),
                            Div('doctor_anestesia_1', css_class='col-4', ),
                            Div('nurse_1', css_class='col-4', ),
                            css_class='row'
                        ),
                        'medicine_description_1',
                    ),
                    # Tab(_('Английский'),
                    #     Div('diagnosis_0', css_class='col-12',),
                    #     Div('department_surgery_0', css_class='col-12', ),
                    #     Div(
                    #         Div('doctor_surgery_0', css_class='col-4', ),
                    #         Div('doctor_anestesia_0', css_class='col-4', ),
                    #         Div('nurse_0', css_class='col-4', ),
                    #         css_class='row'
                    #     ),
                    #     'medicine_description_0',
                    # ),
                    # css_class='',
                ),
                Field('patient', type='hidden'),
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


class SurgeryCreateStepTwoForm(SurgeryPatientEditForm):
    new_patient_id = forms.IntegerField(required=False)
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all()[:1],
        initial=None,
        required=False)

    def save(self, commit=True, patient_info=None):
        if isinstance(patient_info, (int, str)):
            patient = Patient.objects.get(pk=patient_info)
        else:
            p = patient_info
            patient = Patient(
                fullname_0=p.get('fullname_0'),
                fullname_1=p.get('fullname_1'),
                fullname_2=p.get('fullname_2'),
                comment_1=p.get('comment_1'),
                comment_2=p.get('fcomment2'),
                address_0=p.get('address_0'),
                address_1=p.get('address_1'),
                comment_0=p.get('comment_0'),
                address_2=p.get('address_2'),
                city_id=p.get('city.id', None),
                sex_id=p.get('sex.id', None),
                education_institution_id=p.get('education_institution.id', None),
                date_birthday=p.get('date_birthday'),
            )
            patient.save()
        self.instance.patient_id = patient.id
        return super().save(commit=commit)


class SurgeryCreateStepTwoForm_orig(forms.ModelForm):
    new_patient_id = forms.IntegerField(required=False)

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all()[:1],
        initial=-1,
        required=False)

    diagnosis_0 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    diagnosis_1 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    diagnosis_2 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))

    hospital_therapy = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                              required=True,
                                              initial=None,
                                              label=_('Больница, проводящая лечение'),
                                              # widget=forms.Select(attrs={'class': 'text-input'}),
                                              widget=Select2(select2attrs={'width': '100%', 'class': 'text-input'})
                                              )
    hospital_surgery = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                              required=True,
                                              initial=None,
                                              label=_('Больница, где проводится операция'),
                                              # widget=forms.Select(attrs={'class': 'text-input'}),
                                              widget=Select2(select2attrs={'width': '100%', 'class': 'text-input'})
                                              )
    surgery_type = forms.ModelChoiceField(queryset=SurgeryType.objects.all(),
                                              required=False,
                                              initial=None,
                                              label=_('Тип операции'),
                                              widget=Select2(select2attrs={'width': '100%'}),
                                              )
    department_surgery_0 = forms.CharField(required=False, label=_('Отделение'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    department_surgery_1 = forms.CharField(required=False, label=_('Отделение'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    department_surgery_2 = forms.CharField(required=False, label=_('Отделение'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))

    income_date = forms.DateField(
                                  widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                  required=False,
                                  label=_('Дата госпитализации'),
                                  )
    surgery_date = forms.DateField(
                                widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                required=False,
                                label=_('Дата операции'),
                                )
    exit_date = forms.DateField(
                                widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                required=False,
                                label=_('Дата выписки'),
                                )

    doctor_surgery_0 = forms.CharField(required=False,
                                            label=_('Оперировавший врач'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))
    doctor_surgery_1 = forms.CharField(required=False,
                                            label=_('Оперировавший врач'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))
    doctor_surgery_2 = forms.CharField(required=False,
                                            label=_('Оперировавший врач'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))
    doctor_anestesia_0 = forms.CharField(required=False,
                                            label=_('Анестезиолог'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))
    doctor_anestesia_1 = forms.CharField(required=False,
                                            label=_('Анестезиолог'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))
    doctor_anestesia_2 = forms.CharField(required=False,
                                            label=_('Анестезиолог'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))
    nurse_0 = forms.CharField(required=False,
                                            label=_('Медсестра'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))
    nurse_1 = forms.CharField(required=False,
                                            label=_('Медсестра'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))
    nurse_2 = forms.CharField(required=False,
                                            label=_('Медсестра'),
                                            widget=forms.TextInput(attrs={'class': 'text-input'}))

    medicine_description_0 = forms.CharField(required=False,
                                            label=_('Используемые медикаменты'),
                                            widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    medicine_description_1 = forms.CharField(required=False,
                                            label=_('Используемые медикаменты'),
                                            widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    medicine_description_2 = forms.CharField(required=False,
                                            label=_('Используемые медикаменты'),
                                            widget=forms.Textarea(attrs={'rows':3, 'cols':60}))

    price_man = forms.DecimalField(max_digits=19, decimal_places=2,
                                   label=_('Стоимость'),
                                   required=False,
                                   widget=forms.NumberInput())

    additional_info_0 = forms.CharField(required=False,
                                            label=_('Дополнительно'),
                                            widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    additional_info_1 = forms.CharField(required=False,
                                            label=_('Дополнительно'),
                                            widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    additional_info_2 = forms.CharField(required=False,
                                            label=_('Дополнительно'),
                                            widget=forms.Textarea(attrs={'rows':3, 'cols':60}))

    class Meta:
        model = PatientSurgery
        fields = '__all__'

    def save(self, commit=True, patient_info=None):
        if isinstance(patient_info, int):
            patient = Patient.objects.get(pk=patient_info)
        else:
            p = patient_info
            patient = Patient(
                fullname_0=p.get('fullname_0'),
                fullname_1=p.get('fullname_1'),
                fullname_2=p.get('fullname_2'),
                comment_1=p.get('comment_1'),
                comment_2=p.get('fcomment2'),
                address_0=p.get('address_0'),
                address_1=p.get('address_1'),
                comment_0=p.get('comment_0'),
                address_2=p.get('address_2'),
                city_id=p.get('city.id', None),
                sex_id=p.get('sex.id', None),
                education_institution_id=p.get('education_institution.id', None),
                date_birthday=p.get('date_birthday'),
            )
            patient.save()
        self.instance.patient_id = patient.id
        return super().save(commit=commit)

class PatientSurgerySearchForm(forms.Form):
    patient_name = forms.CharField(required=False, label=_('Пациент'),
                               widget=forms.TextInput(attrs={'placeholder': _('Пациент'), })
                               )
    doctor_name = forms.CharField(required=False, label=_('Врач'),
                               widget=forms.TextInput(attrs={'placeholder': _('Врач'), })
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
                                    label=_('Период (дата операции)'),
                                    widget=forms.Select(attrs={'onchange': 'setDates()'}))
    surgery_type = forms.ModelChoiceField(queryset=SurgeryType.objects.all(),
                                              required=False,
                                              initial=None,
                                              label=_('Тип операции'),
                                              widget=Select2(select2attrs={'width': '100%'}),
                                              )
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                      required=False,
                                      initial=None,
                                      label=_('Больница'),
                                      # widget=forms.Select(attrs={'class': 'text-input'}),
                                      widget=Select2(select2attrs={'width': '100%', 'class': 'text-input'})
                                      )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('date_period', css_class='col-4', ),
                    Div('date_start', css_class='col-4', ),
                    Div('date_end', css_class='col-4', ),
                    css_class='row'
                ),
                Div(
                    Div('patient_name', css_class='col-6', ),
                    Div('doctor_name', css_class='col-6', ),
                    css_class='row'
                ),
                Div(
                    Div('surgery_type', css_class='col-4', ),
                    Div('hospital', css_class='col-6', ),
                    Div(
                        FormActions(
                            Submit('search', _('Найти')),
                        ),
                        css_class='col-2 align-self-end',
                    ),
                    css_class='row'
                ),
                css_class='card card-body',
            ),
        )
