from django.db.models import Q
from django.urls import reverse_lazy, resolve
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from health.utils import get_data_lang
from .models import PatientResolution
from .forms import PatientResolutionForm, PatientResolutionSearchForm
from health.settings import LIST_PAGE_SIZE


class PatientResolutionListView(ListView):
    queryset = PatientResolution.objects.order_by('-created_at')
    template_name = 'resolution/resolution_list.html'
    paginate_by = LIST_PAGE_SIZE
    context_object_name = 'resolution_list'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['form'] = PatientResolutionSearchForm()
        return context

    def post(self, request, *args, **kwargs):
        fullname = request.POST.get('fullname')

        if fullname is None:
            self.object_list = PatientResolution.objects.order_by('-created_at')
        else:
            if get_data_lang() == 'en':
                self.object_list = PatientResolution.objects.filter(Q(lastname_0__icontains=fullname) |
                                                                    Q(resolution_name_0__icontains=fullname))\
                                                            .order_by('lastname_0', 'resolution_name_0')
            elif get_data_lang() == 'tk':
                self.object_list = PatientResolution.objects.filter(Q(lastname_2__icontains=fullname) |
                                                                    Q(resolution_name_2__icontains=fullname))\
                                                            .order_by('lastname_2', 'resolution_name_2')
            else:
                self.object_list = PatientResolution.objects.filter(Q(lastname_1__icontains=fullname) |
                                                                    Q(resolution_name_1__icontains=fullname))\
                                                            .order_by('lastname_1', 'resolution_name_1')
        year = request.POST.get('year_birthday', '')
        if len(year) > 0:
            self.object_list = self.object_list.filter(date_birthday__year=year)

        return self.render_to_response(self.get_context_data())


class PatientResolutionCreateFormView(CreateView):
    template_name = 'resolution/resolution_edit.html'
    form_class = PatientResolutionForm
    success_url = reverse_lazy('resolutions:resolution_list')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class PatientResolutionEditFormView(UpdateView):
    template_name = 'resolution/resolution_edit.html'
    form_class = PatientResolutionForm
    model = PatientResolution
    success_url = reverse_lazy('resolutions:resolution_list')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
