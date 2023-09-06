from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import PatientTherapyListView, TherapyCreateStepOneView, TherapyCreateStepTwoView, \
    TherapyCreateStepOneViewWithID, TherapyEditView


app_name = 'therapy'

urlpatterns = [
    path('list/', login_required(PatientTherapyListView.as_view()), name='therapy_list'),
    path('list_period/<str:date_start>/<str:date_end>/',
         login_required(PatientTherapyListView.as_view()), name='therapy_list_period'),
    path('create_one/', login_required(TherapyCreateStepOneView.as_view()), name='create_one'),
    path('create_one_id/<int:id>/', login_required(TherapyCreateStepOneViewWithID.as_view()), name='create_one_id'),
    path('create_two/', login_required(TherapyCreateStepTwoView.as_view()), name='create_two'),
    path('edit/<int:pk>/', login_required(TherapyEditView.as_view()), name='therapy_edit'),
]