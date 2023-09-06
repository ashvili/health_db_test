from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils import translation
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, FormView, PasswordChangeView
from django.contrib.auth import logout, update_session_auth_hash
from django.utils.translation import gettext as _

from health.settings import LANGUAGE_SESSION_KEY, LANGUAGE_COOKIE_NAME
from .forms import AsdUserCreationForm, LoginUserForm, AsdUserChangeForm, AsdPasswordChangeForm
from .models import AsdUser


class AsdUserChangeView(UpdateView):
    form_class = AsdUserChangeForm
    success_url = reverse_lazy('main_page:main_page')
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = _('Профайл')
        return context
    def get_queryset(self):
        print('get_queryset')
        return AsdUser.objects.filter(pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        key = LANGUAGE_SESSION_KEY
        if form.cleaned_data.get('ui_lang'):
            if form.cleaned_data.get('ui_lang') == '0':
                lng = 'en'
            elif form.cleaned_data.get('ui_lang') == '1':
                lng = 'ru'
            else:
                lng = 'tk'
        # self.request.session['_language'] = lng
        # self.request.session['django_language'] = lng
        self.request.session[key] = lng
        translation.activate(lng)
        response = super().form_valid(form)
        response.set_cookie(LANGUAGE_COOKIE_NAME, lng)
        return response



class SignUpView(CreateView):
    model = AsdUser
    form_class = AsdUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data()
        context['title'] = _('Регистрация')
        return context

class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    def get_success_url(self):
        return reverse_lazy('main_page:main_page')
    def get_context_data(self, **kwargs):
        context = super(LoginUserView, self).get_context_data()
        context['title'] = _('Вход')
        return context

def logout_user(request):
    logout(request)
    return redirect('users:login')


class PasswordChangeView(LoginRequiredMixin, FormView):
    model = AsdUser
    form_class = AsdPasswordChangeForm
    template_name = 'users/password_change.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Изменить пароль')
        return context

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super(PasswordChangeView, self).form_valid(form)

    def get_success_url(self):
        url = super().get_success_url()
        return reverse_lazy('users:profile', self.request.user.id)
