from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Fieldset, MultiField, Div, Field
from crispy_forms.bootstrap import FormActions, TabHolder, Tab
from django.forms import PasswordInput

from .models import AsdUser


class AsdUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label=_('Имя'), widget=forms.TextInput(attrs={'class': 'form-input form-control'}))
    last_name = forms.CharField(label=_('Фамилия'), widget=forms.TextInput(attrs={'class': 'form-input form-control'}))
    username = forms.CharField(label=_('Логин'), widget=forms.TextInput(attrs={'class': 'form-input form-control'}))
    email = forms.CharField(label=_('Емейл'), widget=forms.EmailInput(attrs={'class': 'form-input form-control'}))
    password1 = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-input form-control'}))
    password2 = forms.CharField(label=_('Подтверждение пароля'), widget=forms.PasswordInput(attrs={'class': 'form-input form-control'}))

    class Meta:
        model = AsdUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class AsdUserChangeForm(UserChangeForm):
    LANGS = (
        # (0, _('Английский')),
        (1, _('Русский')),
        (2, _('Туркменский')),
    )

    username = forms.CharField(label=_('Логин'), widget=forms.TextInput())
    email = forms.CharField(label=_('Емейл'), widget=forms.EmailInput())
    data_lang = forms.ChoiceField(choices=LANGS, label=_('Язык данных'), )
    ui_lang = forms.ChoiceField(choices=LANGS, label=_('Язык интерфейса'), )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'username',
            'email',
            Div(
                Div('data_lang', css_class='col'),
                Div('ui_lang', css_class='col'),
                css_class='row',
            ),
            FormActions(
                Submit('save', _('Сохранить')),
                Button('cancel', _('Назад'), onclick='history.back()', css_class ="btn btn-secondary")
            )
        )

    class Meta:
        model = AsdUser
        fields = ['username', 'email', 'data_lang', 'ui_lang']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label=_('Логин'), widget=forms.TextInput(attrs={'class': 'form-input form-control'}))
    password = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-input form-control'}))


class AsdPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label=_('Текущий пароль'),
                             widget=PasswordInput(attrs={
                                 'class': 'form-control'}),
                             error_messages={
                                 'required': _('Необходимо ввести текущий пароль')})

    new_password1 = forms.CharField(required=True, label=_('Новый пароль'),
                              widget=PasswordInput(attrs={
                                  'class': 'form-control'}),
                              error_messages={
                                  'required': _('Необходимо ввести новый пароль')})
    new_password2 = forms.CharField(required=True, label=_('Повтор (новый пароль))'),
                              widget=PasswordInput(attrs={
                                  'class': 'form-control'}),
                              error_messages={
                                  'required': _('Необходимо ввести новый пароль повторно')})