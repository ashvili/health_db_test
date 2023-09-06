from datetime import datetime, date

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView
from django.utils.translation import gettext as _

from health.settings import LIST_PAGE_SIZE
from health.utils import get_data_lang
from patients.models import Patient
from patients.forms import PatientFormEmpty
from surgery.forms import SurgeryCreateStepTwoForm, SurgeryPatientEditForm, PatientSurgerySearchForm
from surgery.models import PatientSurgery


class PatientSurgeryListView(ListView):
    queryset = PatientSurgery.objects.order_by('-created_at')
    template_name = 'surgery/surgery_list.html'
    paginate_by = LIST_PAGE_SIZE
    context_object_name = 'surgery_list'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['form'] = PatientSurgerySearchForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = PatientSurgery.objects.order_by('-created_at')

        patient_name = request.POST.get('patient_name', '')
        if len(patient_name) > 0:
            if get_data_lang() == 'en':
                self.object_list = self.object_list.filter(patient__fullname_0__icontains=patient_name)
            elif get_data_lang() == 'tk':
                self.object_list = self.object_list.filter(patient__fullname_2__icontains=patient_name)
            else:
                self.object_list = self.object_list.filter(patient__fullname_1__icontains=patient_name)

        doctor_name = request.POST.get('doctor_name', '')
        if len(doctor_name) > 0:
            if get_data_lang() == 'en':
                self.object_list = self.object_list.filter(doctor_surgery_0__icontains=doctor_name)
            elif get_data_lang() == 'tk':
                self.object_list = self.object_list.filter(doctor_surgery_2__icontains=doctor_name)
            else:
                self.object_list = self.object_list.filter(doctor_surgery_1__icontains=doctor_name)

        date_start = request.POST.get('date_start', '')
        if len(date_start) > 0:
            self.object_list = self.object_list.filter(surgery_date__gte=date_start)
        date_end = request.POST.get('date_end', '')
        if len(date_end) > 0:
            self.object_list = self.object_list.filter(surgery_date__lte=date_end)

        surgery_type = request.POST.get('surgery_type', '')
        if len(surgery_type) > 0:
            self.object_list = self.object_list.filter(surgery_type_id=int(surgery_type))

        hospital = request.POST.get('hospital', '')
        if len(hospital) > 0:
            self.object_list = self.object_list.filter(hospital_surgery__id=int(hospital))

        return self.render_to_response(self.get_context_data())

    def get(self, request, *args, **kwargs):
        self.object_list = PatientSurgery.objects.order_by('-created_at')

        date_start = kwargs.get('date_start', '')
        if len(date_start) > 0:
            self.object_list = self.object_list.filter(surgery_date__gte=date_start)
        date_end = kwargs.get('date_end', '')
        if len(date_end) > 0:
            self.object_list = self.object_list.filter(surgery_date__lte=date_end)

        return self.render_to_response(self.get_context_data())


class SurgeryCreateStepOneView(FormView):
    form_class = PatientFormEmpty
    template_name = 'create_one.html'
    success_url = reverse_lazy('surgery:create_two')

    def form_valid(self, form):
        if form.cleaned_data.get('id'):
            self.request.session['patient_id'] = form.cleaned_data.get('id')
            try:
                del self.request.session['patient']
            except:
                pass
        else:
            try:
                del self.request.session['patient_id']
            except:
                pass
            fields = {}
            for field in list(form.declared_fields):
                if (field == 'csrfmiddlewaretoken') or (form.cleaned_data.get(field) is None):
                    pass
                elif field in ('city', 'sex', 'education_institution'):
                    fields[f'{field}.id'] = form.cleaned_data.get(field).id
                elif isinstance(form.cleaned_data.get(field), (datetime, date)):
                    fields[field] = form.cleaned_data.get(field).isoformat()
                else:
                    fields[field] = form.cleaned_data.get(field)
            self.request.session['patient'] = fields
        return super().form_valid(form)


class SurgeryCreateStepOneViewWithID(FormView):
    form_class = PatientFormEmpty
    template_name = 'create_one.html'
    success_url = reverse_lazy('surgery:create_two')

    def get_initial(self):
        initial = super().get_initial()
        try:
            patient = Patient.objects.get(id=self.kwargs['id'])
            for f in patient._meta.fields:
                if f.name in self.form_class.base_fields:
                    initial[f.name] = getattr(patient, f.name, None)
        finally:
            return initial

    def form_valid(self, form):
        if form.cleaned_data.get('id'):
            self.request.session['patient_id'] = form.cleaned_data.get('id')
            try:
                del self.request.session['patient']
            except:
                pass
        else:
            try:
                del self.request.session['patient_id']
            except:
                pass
            fields = {}
            for field in list(form.declared_fields):
                if (field == 'csrfmiddlewaretoken') or (form.cleaned_data.get(field) is None):
                    pass
                elif field in ('city', 'sex', 'education_institution'):
                    fields[f'{field}.id'] = form.cleaned_data.get(field).id
                elif isinstance(form.cleaned_data.get(field), (datetime, date)):
                    fields[field] = form.cleaned_data.get(field).isoformat()
                else:
                    fields[field] = form.cleaned_data.get(field)
            self.request.session['patient'] = fields
        return super().form_valid(form)


class SurgeryCreateStepTwoView(FormView):
    form_class = SurgeryCreateStepTwoForm
    template_name = 'create_two.html'
    success_url = reverse_lazy('surgery:surgery_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Операция')
        return context

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        if self.request.GET.get('patient_id', None):
            therapy = form.save(patient_info=int(self.request.GET.get('patient_id')))
        else:
            therapy = form.save(patient_info=self.request.session.get('patient'))
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self):
        initial = super().get_initial()
        try:
            if self.request.GET.get('patient_id'):
                patient = Patient.objects.get(id=self.request.GET.get('patient_id'))
                initial['patient_id'] = patient
        finally:
            return initial


class SurgeryEditView(UpdateView):
    form_class = SurgeryPatientEditForm
    template_name = 'create_two.html'
    success_url = reverse_lazy('surgery:surgery_list')
    model = PatientSurgery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Операция')
        return context

    def form_invalid(self, form):
        print(form.errors)
        print(form.cleaned_data.get('id'))
        return super().form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)