from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import DictsView, CityListView, CityEditView, CityCreateView, CityDeleteView, \
    EtrapListView, EtrapEditView, EtrapCreateView, EtrapDeleteView, \
    Education_institutionListView, Education_institutionEditView, Education_institutionCreateView, \
    Education_institutionDeleteView, OrganizationListView, OrganizationEditView, OrganizationCreateView, \
    OrganizationDeleteView, HospitalListView, HospitalEditView, HospitalCreateView, HospitalDeleteView, DoctorListView, \
    DoctorEditView, DoctorCreateView, DoctorDeleteView, UnitListView, UnitEditView, UnitCreateView, UnitDeleteView, \
    load_cities, SurgeryTypeListView, SurgeryTypeEditView, SurgeryTypeDeleteView, SurgeryTypeCreateView

app_name = 'dicts'

urlpatterns = [
    path('', login_required(DictsView.as_view()), name='dicts_list'),

    path('city/', login_required(CityListView.as_view()), name='city_list'),
    path('city/edit/<int:pk>/', login_required(CityEditView.as_view()), name='city_edit'),
    path('city/delete/<int:pk>/', login_required(CityDeleteView.as_view()), name='city_delete'),
    path('city/create/', login_required(CityCreateView.as_view()), name='city_create'),
    path('city/load_cities/', load_cities, name='load_cities'),

    path('etrap/', login_required(EtrapListView.as_view()), name='etrap_list'),
    path('etrap/edit/<int:pk>/', login_required(EtrapEditView.as_view()), name='etrap_edit'),
    path('etrap/delete/<int:pk>/', login_required(EtrapDeleteView.as_view()), name='etrap_delete'),
    path('etrap/create/', login_required(EtrapCreateView.as_view()), name='etrap_create'),

    path('education/', login_required(Education_institutionListView.as_view()), name='education_list'),
    path('education/edit/<int:pk>/', login_required(Education_institutionEditView.as_view()), name='education_edit'),
    path('education/delete/<int:pk>/', login_required(Education_institutionDeleteView.as_view()), name='education_delete'),
    path('education/create/', login_required(Education_institutionCreateView.as_view()), name='education_create'),

    path('organization/', login_required(OrganizationListView.as_view()), name='organization_list'),
    path('organization/edit/<int:pk>/', login_required(OrganizationEditView.as_view()), name='organization_edit'),
    path('organization/delete/<int:pk>/', login_required(OrganizationDeleteView.as_view()), name='organization_delete'),
    path('organization/create/', login_required(OrganizationCreateView.as_view()), name='organization_create'),

    path('hospital/', login_required(HospitalListView.as_view()), name='hospital_list'),
    path('hospital/edit/<int:pk>/', login_required(HospitalEditView.as_view()), name='hospital_edit'),
    path('hospital/delete/<int:pk>/', login_required(HospitalDeleteView.as_view()), name='hospital_delete'),
    path('hospital/create/', login_required(HospitalCreateView.as_view()), name='hospital_create'),

    path('doctor/', login_required(DoctorListView.as_view()), name='doctor_list'),
    path('doctor/edit/<int:pk>/', login_required(DoctorEditView.as_view()), name='doctor_edit'),
    path('doctor/delete/<int:pk>/', login_required(DoctorDeleteView.as_view()), name='doctor_delete'),
    path('doctor/create/', login_required(DoctorCreateView.as_view()), name='doctor_create'),

    path('unit/', login_required(UnitListView.as_view()), name='unit_list'),
    path('unit/edit/<int:pk>/', login_required(UnitEditView.as_view()), name='unit_edit'),
    path('unit/delete/<int:pk>/', login_required(UnitDeleteView.as_view()), name='unit_delete'),

    path('surgery_type/', login_required(SurgeryTypeListView.as_view()), name='surgery_type_list'),
    path('surgery_type/edit/<int:pk>/', login_required(SurgeryTypeEditView.as_view()), name='surgery_type_edit'),
    path('surgery_type/delete/<int:pk>/', login_required(SurgeryTypeDeleteView.as_view()), name='surgery_type_delete'),
    path('surgery_type/create/', login_required(SurgeryTypeCreateView.as_view()), name='surgery_type_create'),
]