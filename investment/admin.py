from django.contrib import admin

from .models import Organization, Investment


admin.site.register(Organization)
admin.site.register(Investment)