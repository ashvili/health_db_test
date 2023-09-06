from django.contrib import admin

from .models import Sex, City, Etrap, Doctor, Hospital, Education_institution, Unit, SurgeryType


admin.site.register(Education_institution)
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(Etrap)
admin.site.register(City)
admin.site.register(Sex)
admin.site.register(Unit)
admin.site.register(SurgeryType)
