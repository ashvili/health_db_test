from django.urls import reverse_lazy, resolve
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView
from django.views.generic.edit import FormMixin

from diagnosis.models import PatientDiagnosis
from health.utils import get_data_lang
from resolution.models import PatientResolution
from surgery.models import PatientSurgery
from .models import Patient
from .forms import PatientForm, PatientSearchForm
from therapy.models import PatientTherapy
from health.settings import LIST_PAGE_SIZE


class PatientListView(ListView):
    queryset = Patient.objects.order_by('-created_at')
    template_name = 'patients/patient_list.html'
    paginate_by = LIST_PAGE_SIZE
    context_object_name = 'patient_list'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['form'] = PatientSearchForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = Patient.objects.order_by('-created_at')

        fullname = request.POST.get('fullname', '')
        if len(fullname) > 0:
            if get_data_lang() == 'en':
                self.object_list = self.object_list.filter(fullname_0__icontains=fullname).order_by('fullname_0')
            elif get_data_lang() == 'tk':
                self.object_list = self.object_list.filter(fullname_2__icontains=fullname).order_by('fullname_2')
            else:
                self.object_list = self.object_list.filter(fullname_1__icontains=fullname).order_by('fullname_1')

        etrap = request.POST.get('etrap', '')
        if len(etrap) > 0:
            self.object_list = self.object_list.filter(city__etrap_id=etrap)

        year = request.POST.get('year_birthday', '')
        if len(year) > 0:
            self.object_list = self.object_list.filter(date_birthday__year=year)

        return self.render_to_response(self.get_context_data())


class PatientCreateFormView(CreateView):
    template_name = 'patients/patient_edit.html'
    form_class = PatientForm
    success_url = reverse_lazy('patients:patient_list')


class PatientEditFormView(UpdateView):
    template_name = 'patients/patient_edit.html'
    form_class = PatientForm
    model = Patient
    success_url = reverse_lazy('patients:patient_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        therapy = PatientTherapy.objects.filter(patient=self.object)
        context['therapy_list'] = therapy if therapy.count() > 0 else None
        surgery = PatientSurgery.objects.filter(patient=self.object)
        context['surgery_list'] = surgery if surgery.count() > 0 else None
        diagnosis = PatientDiagnosis.objects.filter(patient=self.object)
        context['diagnosis_list'] = diagnosis if diagnosis.count() > 0 else None
        resolution = PatientResolution.objects.filter(patient=self.object)
        context['resolution'] = resolution[0] if resolution.count() > 0 else None
        return context

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('patients:patient_list')
