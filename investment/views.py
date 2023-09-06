from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.translation import gettext_lazy as _

from health.settings import LIST_PAGE_SIZE
from health.utils import get_data_lang
from .models import Investment
from .forms import InvestmentForm, InvestmentSearchForm


class InvestmentListView(ListView):
    queryset = Investment.objects.order_by('-created_at')
    template_name = 'investment/investment_list.html'
    paginate_by = LIST_PAGE_SIZE
    context_object_name = 'investment_list'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['title'] = _('Использование средств фонда')
        context['form'] = InvestmentSearchForm()
        return context

    def post(self, request, *args, **kwargs):
        fullname = request.POST.get('fullname', '')
        self.object_list = Investment.objects.order_by('-created_at')
        if len(fullname) > 0:
            if get_data_lang() == 'en':
                self.object_list = self.object_list.filter(investor_0__icontains=fullname)
            elif get_data_lang() == 'tk':
                self.object_list = self.object_list.filter(investor_2__icontains=fullname)
            else:
                self.object_list = self.object_list.filter(investor_1__icontains=fullname)

        date_start = request.POST.get('date_start', '')
        if len(date_start) > 0:
            self.object_list = self.object_list.filter(investment_date__gte=date_start)
        date_end = request.POST.get('date_end', '')
        if len(date_end) > 0:
            self.object_list = self.object_list.filter(investment_date__lte=date_end)

        return self.render_to_response(self.get_context_data())

    def get(self, request, *args, **kwargs):
        self.object_list = Investment.objects.order_by('-created_at')

        date_start = kwargs.get('date_start', '')
        if len(date_start) > 0:
            self.object_list = self.object_list.filter(investment_date__gte=date_start)
        date_end = kwargs.get('date_end', '')
        if len(date_end) > 0:
            self.object_list = self.object_list.filter(investment_date__lte=date_end)

        return self.render_to_response(self.get_context_data())


class InvestmentCreateView(CreateView):
    form_class = InvestmentForm
    template_name = 'investment/investment_edit.html'
    success_url = reverse_lazy('investment:investment_list')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class InvestmentEditView(UpdateView):
    template_name = 'investment/investment_edit.html'
    form_class = InvestmentForm
    model = Investment
    success_url = reverse_lazy('investment:investment_list')