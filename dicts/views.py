import json
from urllib.parse import urlencode

from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, resolve, reverse
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView
from django.utils.translation import gettext as _

from health.settings import LIST_PAGE_SIZE
from .forms import CityForm, EtrapForm, Education_institutionForm, OrganizationForm, HospitalForm, DoctorForm, UnitForm, \
    SurgeryTypeForm
from .models import City, Etrap, Education_institution, Hospital, Doctor, Unit, SurgeryType
from investment.models import Organization


def load_cities(request):
    etrap_id = request.GET.get('etrap')
    cities = City.objects.filter(etrap_id=etrap_id)
    result = list([{'id': c.id, 'name': c.name} for c in cities])
    result = json.dumps(result, ensure_ascii=False)
    return HttpResponse(result,
                        content_type="application/json")
    # return JsonResponse(result, safe=False)

class DictsView(TemplateView):
    template_name = 'dicts/dicts.html'

class CityListView(ListView):
    queryset = City.objects.order_by('name_2')
    template_name = 'dicts/city_list.html'
    paginate_by = LIST_PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['list_title'] = _('Список этрапов (городов)')
        return context


class CityEditView(UpdateView):
    form_class = CityForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:city_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Этрап/город')
        context['error'] = self.request.GET.get('error', None)
        return context

    def get_queryset(self):
        return City.objects.filter(pk=self.kwargs.get('pk'))


class CityCreateView(CreateView):
    form_class = CityForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:city_list')


class CityDeleteView(DeleteView):
    model = City
    success_url = reverse_lazy('dicts:city_list')
    template_name = 'dicts/city_confirm_delete.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, _('Ошибка при удалении: %(e)') % {'e': e,})
            url_str = reverse('dicts:city_edit', kwargs={'pk': self.kwargs['pk']})
            url_str +=f'?error={e}'
            response = HttpResponseRedirect(url_str)
            return response


class EtrapListView(ListView):
    queryset = Etrap.objects.order_by('name_2')
    template_name = 'dicts/city_list.html'
    paginate_by = LIST_PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['list_title'] = _('Список велаятов (городов)')
        return context


class EtrapEditView(UpdateView):
    form_class = EtrapForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:etrap_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Велаят/город')
        context['error'] = self.request.GET.get('error', None)
        return context

    def get_queryset(self):
        return Etrap.objects.filter(pk=self.kwargs.get('pk'))


class EtrapCreateView(CreateView):
    form_class = EtrapForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:etrap_list')

class EtrapDeleteView(DeleteView):
    model = Etrap
    success_url = reverse_lazy('dicts:etrap_list')
    template_name = 'dicts/city_confirm_delete.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, _('Ошибка при удалении: %(e)') % {'e': e,} )
            url_str = reverse('dicts:etrap_edit', kwargs={'pk': self.kwargs['pk']})
            url_str +=f'?error={e}'
            response = HttpResponseRedirect(url_str)
            return response


class Education_institutionListView(ListView):
    queryset = Education_institution.objects.order_by('name_2')
    template_name = 'dicts/city_list.html'
    paginate_by = LIST_PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['list_title'] = _('Список учебных заведений')
        return context


class Education_institutionEditView(UpdateView):
    form_class = Education_institutionForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:education_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Учебное заведение')
        context['error'] = self.request.GET.get('error', None)
        return context

    def get_queryset(self):
        return Education_institution.objects.filter(pk=self.kwargs.get('pk'))


class Education_institutionCreateView(CreateView):
    form_class = Education_institutionForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:education_list')


class Education_institutionDeleteView(DeleteView):
    model = Education_institution
    success_url = reverse_lazy('dicts:education_list')
    template_name = 'dicts/city_confirm_delete.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, _('Ошибка при удалении: %(e)') % {'e': e,})
            url_str = reverse('dicts:education_edit', kwargs={'pk': self.kwargs['pk']})
            url_str +=f'?error={e}'
            response = HttpResponseRedirect(url_str)
            return response


class OrganizationListView(ListView):
    queryset = Organization.objects.order_by('name_2')
    template_name = 'dicts/city_list.html'
    paginate_by = LIST_PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['list_title'] = _('Список организаций/предпринимателей')
        return context


class OrganizationEditView(UpdateView):
    form_class = OrganizationForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:organization_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Организация / поставщик')
        context['error'] = self.request.GET.get('error', None)
        return context

    def get_queryset(self):
        return Organization.objects.filter(pk=self.kwargs.get('pk'))


class OrganizationCreateView(CreateView):
    form_class = OrganizationForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:organization_list')


class OrganizationDeleteView(DeleteView):
    model = Organization
    success_url = reverse_lazy('dicts:organization_list')
    template_name = 'dicts/city_confirm_delete.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, _('Ошибка при удалении: %(e)') % {'e': e, })
            url_str = reverse('dicts:organization_edit', kwargs={'pk': self.kwargs['pk']})
            url_str +=f'?error={e}'
            response = HttpResponseRedirect(url_str)
            return response


class HospitalListView(ListView):
    queryset = Hospital.objects.order_by('name_2')
    template_name = 'dicts/city_list.html'
    paginate_by = LIST_PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['list_title'] = _('Список медицинских учреждений')
        return context


class HospitalEditView(UpdateView):
    form_class = HospitalForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:hospital_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Медицинское учреждение')
        context['error'] = self.request.GET.get('error', None)
        return context

    def get_queryset(self):
        return Hospital.objects.filter(pk=self.kwargs.get('pk'))


class HospitalCreateView(CreateView):
    form_class = HospitalForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:hospital_list')


class HospitalDeleteView(DeleteView):
    model = Organization
    success_url = reverse_lazy('dicts:hospital_list')
    template_name = 'dicts/city_confirm_delete.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, _('Ошибка при удалении: %(e)') % {'e': e,})
            url_str = reverse('dicts:hospital_edit', kwargs={'pk': self.kwargs['pk']})
            url_str +=f'?error={e}'
            response = HttpResponseRedirect(url_str)
            return response


class DoctorListView(ListView):
    queryset = Doctor.objects.order_by('fullname_2')
    template_name = 'dicts/city_list.html'
    paginate_by = LIST_PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['list_title'] = _('Список врачей')
        return context


class DoctorEditView(UpdateView):
    form_class = DoctorForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Врач / медицинский персонал')
        context['error'] = self.request.GET.get('error', None)
        return context

    def get_queryset(self):
        return Doctor.objects.filter(pk=self.kwargs.get('pk'))


class DoctorCreateView(CreateView):
    form_class = DoctorForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:doctor_list')


class DoctorDeleteView(DeleteView):
    model = Organization
    success_url = reverse_lazy('dicts:doctor_list')
    template_name = 'dicts/city_confirm_delete.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, _('Ошибка при удалении: %(e)') % {'e': e,})
            url_str = reverse('dicts:doctor_edit', kwargs={'pk': self.kwargs['pk']})
            url_str +=f'?error={e}'
            response = HttpResponseRedirect(url_str)
            return response


class UnitListView(ListView):
    queryset = Unit.objects.order_by('name_2')
    template_name = 'dicts/city_list.html'
    paginate_by = LIST_PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['list_title'] = _('Единицы измерения')
        return context


class UnitEditView(UpdateView):
    form_class = UnitForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:unit_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Единица измерения')
        context['error'] = self.request.GET.get('error', None)
        return context

    def get_queryset(self):
        return Unit.objects.filter(pk=self.kwargs.get('pk'))


class UnitCreateView(CreateView):
    form_class = UnitForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:unit_list')

class UnitDeleteView(DeleteView):
    model = Unit
    success_url = reverse_lazy('dicts:unit_list')
    template_name = 'dicts/city_confirm_delete.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, _('Ошибка при удалении: %(e)') % {'e': e,})
            url_str = reverse('dicts:unit_edit', kwargs={'pk': self.kwargs['pk']})
            url_str +=f'?error={e}'
            response = HttpResponseRedirect(url_str)
            return response


class SurgeryTypeListView(ListView):
    queryset = SurgeryType.objects.order_by('name_2')
    template_name = 'dicts/city_list.html'
    paginate_by = LIST_PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['list_title'] = _('Типы операций')
        return context


class SurgeryTypeEditView(UpdateView):
    form_class = SurgeryTypeForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:surgery_type_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Тип операции')
        context['error'] = self.request.GET.get('error', None)
        return context

    def get_queryset(self):
        return SurgeryType.objects.filter(pk=self.kwargs.get('pk'))


class SurgeryTypeCreateView(CreateView):
    form_class = SurgeryTypeForm
    template_name = 'dicts/city.html'
    success_url = reverse_lazy('dicts:surgery_type_list')

class SurgeryTypeDeleteView(DeleteView):
    model = SurgeryType
    success_url = reverse_lazy('dicts:surgery_type_list')
    template_name = 'dicts/city_confirm_delete.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, _('Ошибка при удалении: %(e)') % {'e': e,})
            url_str = reverse('dicts:unit_edit', kwargs={'pk': self.kwargs['pk']})
            url_str +=f'?error={e}'
            response = HttpResponseRedirect(url_str)
            return response

