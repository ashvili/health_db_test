import datetime

from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.bootstrap import FormActions, TabHolder, Tab, InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Fieldset, MultiField, Div, Field
from easy_select2 import Select2

from .models import Patient
from dicts.models import City, Sex, Education_institution, Etrap


class PatientForm(forms.ModelForm):
    id = forms.IntegerField(disabled=True, required=False)
    date_birthday = forms.DateField(
                                    widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                    required=False, label=_('Дата рождения'),
                                   )
    fullname_0 = forms.CharField(required=False, label=_('Имя'), widget=forms.TextInput())
    fullname_1 = forms.CharField(required=False, label=_('Имя'), widget=forms.TextInput())
    fullname_2 = forms.CharField(required=False, label=_('Имя'), widget=forms.TextInput())

    address_0 = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label=_('Адрес'))
    address_1 = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label=_('Адрес'))
    address_2 = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label=_('Адрес'))

    etrap = forms.ModelChoiceField(queryset=Etrap.objects.all(), initial=None,
                                   required=False, label=_('Велаят/город'),
                                   widget=forms.Select(attrs={'width': '100%'}))

    city = forms.ModelChoiceField(queryset=City.objects.all(), initial=None,
                                  required=False, label=_('Этрап/город'),
                                  widget=Select2(select2attrs={'width': '100%'}))

    sex = forms.ModelChoiceField(queryset=Sex.objects.all(), initial=None, required=False, label=_('Пол'),
                                 empty_label='')
    education_institution = forms.ModelChoiceField(queryset=Education_institution.objects.all(),
                                                   initial=None, required=False, label=_('Уч. заведение'),
                                                   widget=Select2(select2attrs={'width': '100%'}))

    class Meta:
        model = Patient
        fields = [
            'id',
            'fullname_0', 'fullname_1', 'fullname_2',
            'address_0', 'address_1', 'address_2',
            'etrap', 'city', 'sex', 'education_institution', 'date_birthday',
        ]
        widgets = {
            'fullname_0': forms.Textarea(attrs={'class': 'text-input'}),
            'fullname_1': forms.Textarea(attrs={'class': 'text-input'}),
            'fullname_2': forms.Textarea(attrs={'class': 'text-input'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_class = 'card'
        # self.helper.label_class = 'col-4'
        self.helper.layout = Layout(
            Div(
                TabHolder(
                    Tab(_('Туркменский'),
                        'fullname_2',
                        Div(
                            Div('etrap', css_class='col-2', ),
                            Div('city', css_class='col-4', ),
                            Div('address_2', css_class='col-6', ),
                        css_class='row'),
                        Div(
                            Div('date_birthday', css_class='col-3', ),
                            Div('sex', css_class='col-3', ),
                            Div('education_institution', css_class='col-6', ),
                            css_class='row'),
                        ),
                    Tab(_('Русский'),
                        'fullname_1',
                        'address_1',
                        ),
                    # Tab(_('Английский'),
                    #     'fullname_0',
                    #     'address_0',
                    #     ),
                ),
                FormActions(
                    Submit('save', _('Сохранить')),
                    # Button('delete', 'Удалить',
                    #        onclick='window.location.href = "{}";'.format(
                    #            reverse('dicts:city_delete', kwargs={'pk': self.instance.pk})),
                    #        css_class ="btn btn-danger"
                    #        ) if self.instance.pk else HTML(''),
                    Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
                ),
                css_class='form card col-8',
            ),
        )


class PatientFormEmpty(forms.Form):
    id = forms.IntegerField(disabled=True, required=False)
    date_birthday = forms.DateField(
                                    widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                    required=False, label=_('Дата рождения'),
                                   )
    fullname_0 = forms.CharField(required=False, label=_('Имя'), widget=forms.TextInput())
    fullname_1 = forms.CharField(required=False, label=_('Имя'), widget=forms.TextInput())
    fullname_2 = forms.CharField(required=False, label=_('Имя'), widget=forms.TextInput())

    address_0 = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label='Адрес')
    address_1 = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label='Адрес')
    address_2 = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label='Адрес')

    city = forms.ModelChoiceField(queryset=City.objects.all(), initial=None,
                                  required=False, label=_('Город'),
                                  widget=Select2(select2attrs={'width': '100%'}))
    sex = forms.ModelChoiceField(queryset=Sex.objects.all(), initial=None, required=False, label='Пол',
                                 empty_label='')
    education_institution = forms.ModelChoiceField(queryset=Education_institution.objects.all(),
                                                   initial=None, required=False, label=_('Уч. заведение'),
                                                   widget=Select2(select2attrs={'width': '100%'}))

    class Meta:
        model = Patient
        fields = [
            'id',
            'fullname_0', 'fullname_1', 'fullname_2',
            'address_0', 'address_1', 'address_2',
            'city', 'sex', 'education_institution', 'date_birthday',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_class = 'card'
        # self.helper.label_class = 'col-lg-3'
        self.helper.layout = Layout(
            Div(
                TabHolder(
                    Tab(_('Туркменский'),
                        'fullname_2',
                        Div(
                            Div('city', css_class='col-4', ),
                            Div('address_2', css_class='col-8', ),
                        css_class='row'),
                        Div(
                            Div('date_birthday', css_class='col-3', ),
                            Div('sex', css_class='col-3', ),
                            Div('education_institution', css_class='col-6', ),
                            css_class='row'),
                        ),
                    Tab(_('Русский'),
                        'fullname_1',
                        'address_1',

                        ),
                    # Tab(_('Английский'),
                    #     'fullname_0',
                    #     'address_0',
                    #     ),
                ),
                FormActions(
                    Submit('save', _('Сохранить')),
                    # Button('delete', 'Удалить',
                    #        onclick='window.location.href = "{}";'.format(
                    #            reverse('dicts:city_delete', kwargs={'pk': self.instance.pk})),
                    #        css_class ="btn btn-danger"
                    #        ) if self.instance.pk else HTML(''),
                    Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
                ),
                css_class='form card col-8',
            ),
        )

class PatientSearchForm(forms.Form):
    YEARS = [(None, _('Год рождения')), ] + [(y, str(y)) for y in range(2000, datetime.date.today().year + 1)]

    fullname = forms.CharField(required=False, label='', #_('Имя'),
                               widget=forms.TextInput(attrs={'placeholder': _('Имя пациента'), })
                               )
    etrap = forms.ModelChoiceField(queryset=Etrap.objects.all(), initial=None,
                                   required=False, label='',#_('Велаят/город'),
                                   empty_label=_('Велаят/город'),
                                   widget=forms.Select(attrs={'width': '100%', }))
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
                    Div('fullname', css_class='col-5 align-self-end', ),
                    Div('year_birthday', css_class='col-3 align-self-end', ),
                    Div('etrap', css_class='col-3 align-self-end', ),
                    Div(
                        FormActions(
                            Submit('search', _('Найти')),
                        ),
                        css_class='col-1 align-self-end',
                    ),
                    css_class='row'),
                css_class='',
            ),
        )
