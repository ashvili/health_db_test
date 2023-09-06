from django import forms
from crispy_forms.bootstrap import FormActions, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Fieldset, MultiField, Div, Field
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _

from easy_select2 import Select2

from .models import Etrap, City, Education_institution, Hospital, Doctor, Sex, Unit, SurgeryType
from investment.models import Organization


class CityForm(forms.ModelForm):
    name_0 = forms.CharField(label=_('Название'), required=False)
    name_1 = forms.CharField(label=_('Название'), required=False)
    name_2 = forms.CharField(label=_('Название'))
    etrap = forms.ModelChoiceField(queryset=Etrap.objects.all(), label=_('Этрап'), widget=forms.Select(attrs={'width': '100%'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Туркменский'),
                    Column('name_2', css_class='form-group'),
                    ),
                Tab(_('Русский'),
                    Column('name_1', css_class='form-group'),
                    ),
                # Tab(_('Английский'),
                #     Column('name_0', css_class='form-group'),
                #     ),
                css_class='col col-5',
            ),
            Column('etrap', css_class='form-group'),
            FormActions(
                Submit('save', _('Сохранить')),
                Button('delete', _('Удалить'),
                       onclick='window.location.href = "{}";'.format(
                           reverse('dicts:city_delete', kwargs={'pk': self.instance.pk})),
                       css_class ="btn btn-danger"
                       ) if self.instance.pk else HTML(''),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
            )
        )

    class Meta:
        model = City
        fields = [
            'id', 'etrap',
            'name_0', 'name_1', 'name_2',
        ]


class EtrapForm(forms.ModelForm):
    name_0 = forms.CharField(label=_('Название'), required=False)
    name_1 = forms.CharField(label=_('Название'), required=False)
    name_2 = forms.CharField(label=_('Название'))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Туркменский'),
                    Column('name_2', css_class='form-group col-md-4 mb-0'),
                    ),
                Tab(_('Русский'),
                    Column('name_1', css_class='form-group col-md-4 mb-0'),
                    ),
                # Tab(_('Английский'),
                #     Column('name_0', css_class='form-group col-md-4 mb-0'),
                #     ),
                css_class='col col-5',
            ),
            FormActions(
                Submit('save', _('Сохранить')),
                Button('delete', _('Удалить'),
                       onclick='window.location.href = "{}";'.format(
                           reverse('dicts:etrap_delete', kwargs={'pk': self.instance.pk})),
                       css_class ="btn btn-danger"
                       ) if self.instance.pk else HTML(''),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
            )
        )

    class Meta:
        model = Etrap
        fields = [
            'id', 'name_0', 'name_1', 'name_2',
        ]


class Education_institutionForm(forms.ModelForm):
    name_0 = forms.CharField(label=_('Название'), required=False)
    name_1 = forms.CharField(label=_('Название'), required=False)
    name_2 = forms.CharField(label=_('Название'))
    address_0 = forms.CharField(label=_('Адрес'), required=False,
                                widget=forms.Textarea(attrs={'rows':3, }))
    address_1 = forms.CharField(label=_('Адрес'), required=False,
                                widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    address_2 = forms.CharField(label=_('Адрес'),
                                widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    etrap = forms.ModelChoiceField(queryset=Etrap.objects.all(), label=_('Велаят/город'), required=False, widget=Select2(select2attrs={'width': '100%'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), label=_('Этрап/город'), required=False, widget=Select2(select2attrs={'width': '100%'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Туркменский'),
                    Column('name_2', css_class='form-group '),
                    Column('address_2', css_class='form-group '),
                    ),
                Tab(_('Русский'),
                    Column('name_1', css_class='form-group'),
                    Column('address_1', css_class='form-group '),
                    ),
                # Tab(_('Английский'),
                #     Column('name_0', css_class='form-group'),
                #     Column('address_0', css_class='form-group '),
                #     ),
                css_class='col col-5',
            ),
            'etrap',
            'city',
            FormActions(
                Submit('save', _('Сохранить')),
                Button('delete', _('Удалить'),
                       onclick='window.location.href = "{}";'.format(
                           reverse('dicts:education_delete', kwargs={'pk': self.instance.pk})),
                       css_class ="btn btn-danger"
                       ) if self.instance.pk else HTML(''),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
            )
        )

    class Meta:
        model = Education_institution
        fields = [
            'id', 'name_0', 'name_1', 'name_2',
            'address_0', 'address_1', 'address_2',
            'city', 'etrap',
        ]


class OrganizationForm(forms.ModelForm):
    name_0 = forms.CharField(label=_('Название'), required=False)
    name_1 = forms.CharField(label=_('Название'), required=False)
    name_2 = forms.CharField(label=_('Название'))
    source = forms.BooleanField(label=_('Получатель'), required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Туркменский'),
                    Column('name_2', css_class='form-group'),
                    ),
                Tab(_('Русский'),
                    Column('name_1', css_class='form-group'),
                    ),
                # Tab(_('Английский'),
                #     Column('name_0', css_class='form-group'),
                #     ),
                css_class='',
            ),
            'source',
            FormActions(
                Submit('save', _('Сохранить')),
                Button('delete', _('Удалить'),
                       onclick='window.location.href = "{}";'.format(
                           reverse('dicts:organization_delete', kwargs={'pk': self.instance.pk})),
                       css_class ="btn btn-danger"
                       ) if self.instance.pk else HTML(''),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
            )
        )

    class Meta:
        model = Organization
        fields = [
            'id', 'name_0', 'name_1', 'name_2', 'source',
        ]


class HospitalForm(forms.ModelForm):
    name_0 = forms.CharField(label=_('Название'), required=False)
    name_1 = forms.CharField(label=_('Название'), required=False)
    name_2 = forms.CharField(label=_('Название'))
    address_0 = forms.CharField(label=_('Адрес'), required=False,
                                widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    address_1 = forms.CharField(label=_('Адрес'), required=False,
                                widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    address_2 = forms.CharField(label=_('Адрес'),
                                widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    etrap = forms.ModelChoiceField(queryset=Etrap.objects.all(), label=_('Велаят/город'), required=False, widget=Select2(select2attrs={'width': '100%'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), label=_('Этрап/город'), required=False, widget=Select2(select2attrs={'width': '100%'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Туркменский'),
                    Column('name_2', css_class='form-group'),
                    Column('address_2', css_class=''),
                    ),
                Tab(_('Русский'),
                    Column('name_1', css_class='form-group'),
                    Column('address_1', css_class=''),
                    ),
                # Tab(_('Английский'),
                #     Column('name_0', css_class='form-group'),
                #     Column('address_0', css_class=''),
                #     ),
            css_class='col',
            ),
            Div('etrap', css_class='col'),
            Div('city', css_class='col'),
            FormActions(
                Submit('save', _('Сохранить')),
                Button('delete', _('Удалить'),
                       onclick='window.location.href = "{}";'.format(
                           reverse('dicts:hospital_delete', kwargs={'pk': self.instance.pk})),
                       css_class ="btn btn-danger"
                       ) if self.instance.pk else HTML(''),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
            )
        )

    class Meta:
        model = Hospital
        fields = [
            'id',
            'name_0', 'name_1', 'name_2',
            'address_0', 'address_1', 'address_2',
            'city', 'etrap',
        ]


class DoctorForm(forms.ModelForm):
    fullname_0 = forms.CharField(label=_('Имя Фамилия'), required=False)
    fullname_1 = forms.CharField(label=_('Имя Фамилия'), required=False)
    fullname_2 = forms.CharField(label=_('Имя Фамилия'))
    date_birthday = forms.DateField(label='Дата рожд.',
        widget=forms.NumberInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
        required=False
    )
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                      label=_('Больница'), required=False,
                                      widget=Select2(select2attrs={'width': '100%'}))
    sex = forms.ModelChoiceField(queryset=Sex.objects.all(),
                                 label=_('Пол'), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Туркменский'),
                    Column('fullname_2', css_class='form-group',),
                    ),
                Tab(_('Русский'),
                    Column('fullname_1', css_class='form-group',),
                    ),
                # Tab(_('Английский'),
                #     Column('fullname_0', css_class='form-group',),
                #     ),
            css_class='col',
            ),
            Div(
                Div('sex', css_class='col-3',),
                Div('date_birthday', css_class='col-5',),
                css_class='row'),
            Div(
                Div('hospital', css_class='col-12',),
                css_class='row',),
            FormActions(
                Submit('save', _('Сохранить')),
                Button('delete', _('Удалить'),
                       onclick='window.location.href = "{}";'.format(
                           reverse('dicts:doctor_delete', kwargs={'pk': self.instance.pk})),
                       css_class ="btn btn-danger"
                       ) if self.instance.pk else HTML(''),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary"),
            ),
        )

    class Meta:
        model = Doctor
        fields = [
            'id',
            'fullname_0', 'fullname_1', 'fullname_2',
            'date_birthday', 'hospital', 'sex',
        ]


class UnitForm(forms.ModelForm):
    name_0 = forms.CharField(label=_('Название'), required=False)
    name_1 = forms.CharField(label=_('Название'), required=False)
    name_2 = forms.CharField(label=_('Название'))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Туркменский'),
                    Column('name_2', css_class='form-group'),
                    ),
                Tab(_('Русский'),
                    Column('name_1', css_class='form-group'),
                    ),
                # Tab(_('Английский'),
                #     Column('name_0', css_class='form-group'),
                #     ),
                css_class='col',
            ),
            FormActions(
                Submit('save', _('Сохранить')),
                Button('delete', _('Удалить'),
                       onclick='window.location.href = "{}";'.format(
                           reverse('dicts:etrap_delete', kwargs={'pk': self.instance.pk})),
                       css_class ="btn btn-danger"
                       ) if self.instance.pk else HTML(''),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
            )
        )

    class Meta:
        model = Unit
        fields = [
            'id', 'name_0', 'name_1', 'name_2',
        ]

class SurgeryTypeForm(forms.ModelForm):
    name_0 = forms.CharField(label=_('Название'), required=False)
    name_1 = forms.CharField(label=_('Название'), required=False)
    name_2 = forms.CharField(label=_('Название'))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            TabHolder(
                Tab(_('Туркменский'),
                    Column('name_2', css_class='form-group'),
                    ),
                Tab(_('Русский'),
                    Column('name_1', css_class='form-group'),
                    ),
                # Tab(_('Английский'),
                #     Column('name_0', css_class='form-group'),
                #     ),
                css_class='col',
            ),
            FormActions(
                Submit('save', _('Сохранить')),
                Button('delete', _('Удалить'),
                       onclick='window.location.href = "{}";'.format(
                           reverse('dicts:etrap_delete', kwargs={'pk': self.instance.pk})),
                       css_class ="btn btn-danger"
                       ) if self.instance.pk else HTML(''),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
            )
        )

    class Meta:
        model = SurgeryType
        fields = [
            'id', 'name_0', 'name_1', 'name_2',
        ]


