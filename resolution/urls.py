from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import PatientResolutionListView, PatientResolutionCreateFormView, PatientResolutionEditFormView

app_name = 'resolutions'

urlpatterns = [
    path('list/', login_required(PatientResolutionListView.as_view()), name='resolution_list'),
    path('create/', login_required(PatientResolutionCreateFormView.as_view()), name='resolution_create'),
    path('edit/<int:pk>/', login_required(PatientResolutionEditFormView.as_view()), name='resolution_edit'),
    # path('delete/<int:pk>/', login_required(PatientDeleteView.as_view()), name='patient_delete'),
]