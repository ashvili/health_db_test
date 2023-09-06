from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import PatientListView, PatientCreateFormView, PatientEditFormView, PatientDeleteView

app_name = 'patients'

urlpatterns = [
    path('list/', login_required(PatientListView.as_view()), name='patient_list'),
    path('create/', login_required(PatientCreateFormView.as_view()), name='patient_create'),
    path('edit/<int:pk>/', login_required(PatientEditFormView.as_view()), name='patient_edit'),
    path('delete/<int:pk>/', login_required(PatientDeleteView.as_view()), name='patient_delete'),
]