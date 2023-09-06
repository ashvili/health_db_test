from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from .views import PatientSurgeryListView, SurgeryCreateStepOneView, SurgeryCreateStepOneViewWithID, \
    SurgeryCreateStepTwoView, SurgeryEditView

app_name = 'surgery'

urlpatterns = [
    path('list/', login_required(PatientSurgeryListView.as_view()), name='surgery_list'),
    # re_path('list/(?P<date_start>[^/]+)/(?P<date_end>[^/]+)$',
    path('list_period/<str:date_start>/<str:date_end>/',
         login_required(PatientSurgeryListView.as_view()), name='surgery_list_period'),
    path('create_one/', login_required(SurgeryCreateStepOneView.as_view()), name='create_one'),
    path('create_one_id/<int:id>/', login_required(SurgeryCreateStepOneViewWithID.as_view()), name='create_one_id'),
    path('create_two/', login_required(SurgeryCreateStepTwoView.as_view()), name='create_two'),
    path('edit/<int:pk>/', login_required(SurgeryEditView.as_view()), name='surgery_edit'),
]