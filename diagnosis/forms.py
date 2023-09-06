from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.bootstrap import FormActions, TabHolder, Tab, InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, Div, Field, Hidden
from easy_select2 import Select2

from health import settings
from patients.models import Patient
from dicts.models import Hospital, City, Sex, Education_institution
from .models import PatientDiagnosis


class DiagnosisPatientEditForm(forms.ModelForm):
    diagnosis_0 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3,}))
    diagnosis_1 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3,}))
    diagnosis_2 = forms.CharField(required=True, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3,}))

    diagnosis_description_0 = forms.CharField(required=False,
                                            label=_('Проведенные мероприятия'),
                                            widget=forms.Textarea(attrs={'rows':3,}))
    diagnosis_description_1 = forms.CharField(required=False,
                                            label=_('Проведенные мероприятия'),
                                            widget=forms.Textarea(attrs={'rows':3,}))
    diagnosis_description_2 = forms.CharField(required=True,
                                            label=_('Проведенные мероприятия'),
                                            widget=forms.Textarea(attrs={'rows':3,}))

    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                      required=True,
                                      initial=None,
                                      label=_('Больница, проводящая диагностику'),
                                      widget=Select2(select2attrs={'width': '100%'}),
                                      )

    exit_date = forms.DateField(
                                widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                required=False,
                                label=_('Дата выписки'),
                                )

    doctor_diagnosis_0 = forms.CharField(required=False,
                                         label=_('Осматриваюший врач'),
                                         widget=forms.TextInput())
    doctor_diagnosis_1 = forms.CharField(required=False,
                                         label=_('Осматриваюший врач'),
                                         widget=forms.TextInput())
    doctor_diagnosis_2 = forms.CharField(required=True,
                                         label=_('Осматриваюший врач'),
                                         widget=forms.TextInput())

    price_man = forms.DecimalField(max_digits=19, decimal_places=2,
                                   label=_('Стоимость'),
                                   required=True,
                                   widget=forms.NumberInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                TabHolder(
                    Tab(_('Туркменский'),
                        Div('diagnosis_2', css_class='col-12',),
                        'diagnosis_description_2',
                        Div(
                            Div('hospital', css_class='col-8',),
                            Div('exit_date', css_class='col-4',),
                        css_class='row'),
                        'doctor_diagnosis_2',
                        ),
                    Tab(_('Русский'),
                        'diagnosis_1',
                        'diagnosis_description_1',
                        'doctor_diagnosis_1',
                        ),
                    # Tab(_('Английский'),
                    #     'diagnosis_0',
                    #     'diagnosis_description_0',
                    #     'doctor_diagnosis_0',
                    #     ),
                    # css_class='',
                ),
                Div('price_man', css_class='col-4', ),
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
            css_class='form card col-6',
            ),
        )

    class Meta:
        model = PatientDiagnosis
        fields = [
            'id', 'patient',
            'diagnosis_0', 'diagnosis_1', 'diagnosis_2',
            'hospital', 'exit_date',
            'doctor_diagnosis_0', 'doctor_diagnosis_1', 'doctor_diagnosis_2',
            'diagnosis_description_0', 'diagnosis_description_1', 'diagnosis_description_2',
            'price_man',
        ]


class DiagnosisCreateStepTwoForm(DiagnosisPatientEditForm):
    new_patient_id = forms.IntegerField(required=False)

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all()[:1],
        initial=None,
        required=False)

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


class DiagnosisCreateStepTwoForm_orig(forms.ModelForm):
    new_patient_id = forms.IntegerField(required=False)

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all()[:1],
        initial=-1,
        required=False)

    diagnosis_0 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    diagnosis_1 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    diagnosis_2 = forms.CharField(required=False, label=_('Диагноз'), widget=forms.Textarea(attrs={'rows':3, 'cols':60}))

    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                      required=True,
                                      initial=None,
                                      label=_('Больница, проводящая диагностику'),
                                      # widget=forms.Select(attrs={'class': 'text-input'}),
                                      widget=Select2(select2attrs={'width': '100%', 'class': 'text-input'})
                                      )
    exit_date = forms.DateField(
                                widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                required=False,
                                label=_('Дата выписки'),
                                )

    doctor_diagnosis_0 = forms.CharField(required=False,
                                         label=_('Осматриваюший врач'),
                                         widget=forms.TextInput(attrs={'class': 'text-input'}))
    doctor_diagnosis_1 = forms.CharField(required=False,
                                         label=_('Осматриваюший врач'),
                                         widget=forms.TextInput(attrs={'class': 'text-input'}))
    doctor_diagnosis_2 = forms.CharField(required=False,
                                         label=_('Осматриваюший врач'),
                                         widget=forms.TextInput(attrs={'class': 'text-input'}))

    diagnosis_description_0 = forms.CharField(required=False,
                                              label=_('Проведенные мероприятия'),
                                              widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    diagnosis_description_1 = forms.CharField(required=False,
                                              label=_('Проведенные мероприятия'),
                                              widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    diagnosis_description_2 = forms.CharField(required=False,
                                              label=_('Проведенные мероприятия'),
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
        model = PatientDiagnosis
        fields = [
            'id', 'patient',
            'diagnosis_0', 'diagnosis_1', 'diagnosis_2',
            'hospital', 'exit_date',
            'doctor_diagnosis_0', 'doctor_diagnosis_1', 'doctor_diagnosis_2',
            'price_man',
            'additional_info_0', 'additional_info_1', 'additional_info_2',
        ]

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                TabHolder(
                    Tab(_('Туркменский'),
                        Column('diagnosis_2', css_class='form-group col-md-4 mb-0'),
                        Column('hospital', css_class='col', ),
                        Column('diagnosis_description_2', css_class='col-md-4 mb-0'),
                        Column('exit_date', css_class='col-2', ),
                        Column('doctor_diagnosis_2', css_class='col-md-4 mb-0'),
                        ),
                    Tab(_('Русский'),
                        Column('diagnosis_1', css_class='form-group col-md-4 mb-0'),
                        Column('diagnosis_description_1', css_class='col-md-4 mb-0'),
                        Column('doctor_diagnosis_1', css_class='col-md-4 mb-0'),
                        ),
                    # Tab(_('Английский'),
                    #     Column('diagnosis_0', css_class='form-group col-md-4 mb-0'),
                    #     Column('diagnosis_description_0', css_class='col-md-4 mb-0'),
                    #     Column('doctor_diagnosis_0', css_class='col-md-4 mb-0'),
                    #     ),
                    css_class='col col-10',
                ),
                Row(

                    Column('price_man', css_class='col-2', ),
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


class DiagnosisPatientSearchForm(forms.Form):
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
                                    label=_('Период (дата выписки)'),
                                    widget=forms.Select(attrs={'onchange': 'setDates()'}))
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
                    Div('hospital', css_class='col-6', ),
                    Div(
                        FormActions(
                            Submit('search', _('Найти'), css_class='btn btn-primary'),
                        ),
                        css_class='d-grid gap-2 mx-auto col-6 align-self-end justify-content-begin',
                    ),
                    css_class='row'
                ),
                css_class='card card-body',
            ),
        )
