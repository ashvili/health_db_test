from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import PatientDiagnosisListView, DiagnosisCreateStepOneView, DiagnosisCreateStepOneViewWithID, \
    DiagnosisCreateStepTwoView, DiagnosisEditView

app_name = 'diagnosis'

urlpatterns = [
    path('list/', login_required(PatientDiagnosisListView.as_view()), name='diagnosis_list'),
    path('list_period/<str:date_start>/<str:date_end>/',
         login_required(PatientDiagnosisListView.as_view()), name='diagnosis_list_period'),
    path('create_one/', login_required(DiagnosisCreateStepOneView.as_view()), name='create_one'),
    path('create_one_id/<int:id>/', login_required(DiagnosisCreateStepOneViewWithID.as_view()), name='create_one_id'),
    path('create_two/', login_required(DiagnosisCreateStepTwoView.as_view()), name='create_two'),
    path('edit/<int:pk>/', login_required(DiagnosisEditView.as_view()), name='diagnosis_edit'),
]