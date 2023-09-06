from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AsdUserChangeForm, AsdUserCreationForm
from .models import AsdUser


class AsdUserAdmin(UserAdmin):
    add_form = AsdUserCreationForm
    form = AsdUserChangeForm
    model = AsdUser
    list_display = ['email', 'username',]

admin.site.register(AsdUser, AsdUserAdmin)
