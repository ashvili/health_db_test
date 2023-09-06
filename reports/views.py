import datetime
from dateutil.relativedelta import relativedelta

from django.db import connection
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import TemplateView, FormView, ListView
from django.db.models import Count, Sum
from django.utils.dateparse import parse_date
from django.utils.translation import gettext as _

from diagnosis.models import PatientDiagnosis
from dicts.models import Etrap
from health.utils import SearchViewMixin
from patients.models import Patient
from resolution.models import PatientResolution
from therapy.models import PatientTherapy
from .forms import ReportParametersForm
from surgery.models import PatientSurgery
from .models import ReportByVelayatModel, PatientEvent, ReportByMonthModel


class ReportInfoView(TemplateView):
    template_name = 'reports/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        surgery_total_count = PatientSurgery.objects\
                                            .values('id')\
                                            .annotate(count=Count('id'))
        return context


class ReportPageView(FormView):
    form_class = ReportParametersForm
    template_name = 'reports/reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Отчёты')
        return context

    def get_success_url(self):
        if 'statistic' in self.request.POST:
            return reverse_lazy('reports:report_statistic',
                                kwargs={
                                    'date_start': self.request.POST.get('date_start') or datetime.date(now().year, now().month,  1),
                                    'date_end': self.request.POST.get('date_end') or
                                                datetime.date(now().year, now().month,  1) + \
                                                relativedelta(months=1),
                                    'etrap': self.request.POST.get('etrap', -1) or -1,
                                })
        if 'statistic_by_month' in self.request.POST:
            return reverse_lazy('reports:statistic_by_month',
                                kwargs={
                                    'date_start': self.request.POST.get('date_start') or datetime.date(now().year, now().month,  1),
                                    'date_end': self.request.POST.get('date_end') or
                                                datetime.date(now().year, now().month,  1) + \
                                                relativedelta(months=1),
                                    'etrap': self.request.POST.get('etrap', -1) or -1,
                                })
        if 'statistic_by_velayat' in self.request.POST:
            return reverse_lazy('reports:statistic_by_velayat',
                                kwargs={
                                    'date_start': self.request.POST.get('date_start') or datetime.date(now().year,
                                                                                                       now().month, 1),
                                    'date_end': self.request.POST.get('date_end') or
                                                datetime.date(now().year, now().month, 1) + \
                                                relativedelta(months=1),
                                })
        if 'hospitals' in self.request.POST:
            return reverse_lazy('reports:hospitals',
                                kwargs={
                                    'date_start': self.request.POST.get('date_start') or datetime.date(now().year,
                                                                                                       now().month, 1),
                                    'date_end': self.request.POST.get('date_end') or
                                                datetime.date(now().year, now().month, 1) + \
                                                relativedelta(months=1),
                                })
        return reverse_lazy('reports:reports')


class SearchStatisticView(SearchViewMixin, TemplateView):
    template_name = 'reports/statistic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.init_params()

        context['form'] = ReportParametersForm
        context['title'] = f"{_('Статистика за период')}: {self.kwargs.get('date_start')} / {self.kwargs.get('date_end')}"
        if self.etrap >= 0:
            etrap = Etrap.objects.get(pk=self.etrap)
            if etrap:
                context['title'] += f". {_('Велаят')}: {etrap.name}"

        patients = Patient.objects.filter(created_at__range=(self.date_start, self.date_end))
        if self.etrap > 0:
            patients = patients.filter(city__etrap__id=self.etrap)
        context['add_patient'] = patients.count()
        surgery = PatientSurgery.objects.filter(created_at__range=(self.date_start, self.date_end))
        if self.etrap > 0:
            surgery = surgery.filter(hospital_surgery__etrap__id=self.etrap)
        context['add_surgery'] = surgery.count()
        surgery = PatientSurgery.objects.filter(surgery_date__range=(self.date_start, self.date_end))
        if self.etrap > 0:
            surgery = surgery.filter(hospital_surgery__etrap__id=self.etrap)
        context['total_surgery'] = surgery.aggregate(count=Count('id'), sum=Sum('price_man'))

        therapy = PatientTherapy.objects.filter(created_at__range=(self.date_start, self.date_end))
        if self.etrap > 0:
            therapy = therapy.filter(hospital__etrap__id=self.etrap)
        context['add_therapy'] = therapy.count()
        therapy = PatientTherapy.objects.filter(exit_date__range=(self.date_start, self.date_end))
        if self.etrap > 0:
            therapy = therapy.filter(hospital__etrap__id=self.etrap)
        context['total_therapy'] = therapy.aggregate(count=Count('id'), sum=Sum('price_man'))

        diagnosis = PatientDiagnosis.objects.filter(created_at__range=(self.date_start, self.date_end))
        if self.etrap > 0:
            diagnosis = diagnosis.filter(hospital__etrap__id=self.etrap)
        context['add_diagnosis'] = diagnosis.count()
        diagnosis = PatientDiagnosis.objects.filter(exit_date__range=(self.date_start, self.date_end))
        if self.etrap > 0:
            diagnosis = diagnosis.filter(hospital__etrap__id=self.etrap)
        context['total_diagnosis'] = diagnosis.aggregate(count=Count('id'), sum=Sum('price_man'))

        context['total'] = {'sum': (context['total_surgery']['sum'] or 0) +
                                   (context['total_therapy']['sum'] or 0) +
                                   (context['total_diagnosis']['sum'] or 0),
                            'count': (context['total_surgery']['count'] or 0) +
                                     (context['total_therapy']['count'] or 0) +
                                     (context['total_diagnosis']['count'] or 0),
                            }

        resolution = PatientResolution.objects.filter(created_at__range=(self.date_start, self.date_end))
        context['add_resolution'] = resolution.count()

        return context

    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     context['date_start'] = self.request.POST.get('date_start', '')
    #     context['date_end'] = self.request.POST.get('date_end', '')
    #     context['etrap'] = self.request.POST.get('etrap', '')
    #     return self.render_to_response(context)
    #
    # def get_success_url(self):
    #     if 'statistic' in self.request.POST:
    #         return reverse_lazy('reports:report_statistic',
    #                             kwargs={
    #                                 'date_start': self.request.POST.get('date_start') or datetime.date(now().year, now().month,  1),
    #                                 'date_end': self.request.POST.get('date_end') or
    #                                             datetime.date(now().year, now().month,  1) + \
    #                                             relativedelta(months=1),
    #                                 'etrap': self.request.POST.get('etrap', -1) or -1,
    #                             })
    #     if 'statistic_by_velayat' in self.request.POST:
    #         return reverse_lazy('reports:statistic_by_velayat',
    #                             kwargs={
    #                                 'date_start': self.request.POST.get('date_start') or datetime.date(now().year,
    #                                                                                                    now().month, 1),
    #                                 'date_end': self.request.POST.get('date_end') or
    #                                             datetime.date(now().year, now().month, 1) + \
    #                                             relativedelta(months=1),
    #                             })
    #     return reverse_lazy('reports:reports')

class SearchStatisticByVelayatView(SearchViewMixin, ListView):
    template_name = 'reports/statistic_by_velayat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['form'] = ReportParametersForm
            context['title'] = f"{_('Статистика по велаятам')}: {self.kwargs.get('date_start')} / {self.kwargs.get('date_end')}"
            total = {'surgery_count': sum([r.surgery_count for r in self.object_list]),
                     'surgery_sum': sum([r.surgery_sum for r in self.object_list]),
                     'therapy_count': sum([r.therapy_count for r in self.object_list]),
                     'therapy_sum': sum([r.therapy_sum for r in self.object_list]),
                     'diagnosis_count': sum([r.diagnosis_count for r in self.object_list]),
                     'diagnosis_sum': sum([r.diagnosis_sum for r in self.object_list]),
                     'total_count': sum([r.total_count for r in self.object_list]),
                     'total_sum': sum([r.total_sum for r in self.object_list])}
            context['total'] = total

        finally:
            return context

    def get_queryset(self):
        self.init_params()

        sql_text = 'SELECT etrap_id, etrap_name_0, etrap_name_1, etrap_name_2, ' \
                   'surgery_count, surgery_sum, ' \
                   'therapy_count, therapy_sum, ' \
                   'diagnosis_count, diagnosis_sum, ' \
                   'total_count, total_sum ' \
                   'FROM "get_report_01"(%s::date, %s::date);'

        return ReportByVelayatModel.objects.raw(sql_text, [self.date_start.strftime('%d.%m.%Y'),
                                                           self.date_end.strftime('%d.%m.%Y')])

class SearchHospitalsView(SearchViewMixin, ListView):
    template_name = 'reports/hospitals.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = f"{_('Суммы по больницам')}: {self.kwargs.get('date_start')} / {self.kwargs.get('date_end')}"
            total = {'count': sum([r['count'] for r in self.object_list]),
                     'sum': sum([r['sum'] for r in self.object_list]),
                     'hospital_count': self.object_list.count()}
            context['total'] = total
        finally:
            return context

    def get_queryset(self):
        self.init_params()
        return PatientEvent.objects.values('hospital', 'hospital__name_0', 'hospital__name_1', 'hospital__name_2', )\
            .filter(event_type__in=(0, 1, 2))\
            .filter(event_date__range=(self.date_start, self.date_end))\
            .annotate(sum=Sum('price_man'), count=Count('id')) \
            .order_by('-sum')\
            .all()

class SearchStatisticByMonthView(SearchViewMixin, ListView):
    template_name = 'reports/statistic_by_month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            self.init_params()
            context['title'] = f"{_('Суммы по месяцам')}: {self.kwargs.get('date_start')} / {self.kwargs.get('date_end')}"
            if self.etrap >= 0:
                etrap = Etrap.objects.get(pk=self.etrap)
                if etrap:
                    context['title'] += f". {_('Велаят')}: {etrap.name}"
            total = {'surgery_count': sum([r.surgery_count for r in self.object_list]),
                     'surgery_sum': sum([r.surgery_sum for r in self.object_list]),
                     'therapy_count': sum([r.therapy_count for r in self.object_list]),
                     'therapy_sum': sum([r.therapy_sum for r in self.object_list]),
                     'diagnosis_count': sum([r.diagnosis_count for r in self.object_list]),
                     'diagnosis_sum': sum([r.diagnosis_sum for r in self.object_list]),
                     'total_count': sum([r.total_count for r in self.object_list]),
                     'total_sum': sum([r.total_sum for r in self.object_list])}
            context['total'] = total
        finally:
            return context

    def get_queryset(self):
        self.init_params()
        sql_text = 'SELECT id, month_name, ' \
                   'surgery_count, surgery_sum, ' \
                   'therapy_count, therapy_sum, ' \
                   'diagnosis_count, diagnosis_sum, ' \
                   'total_count, total_sum ' \
                   'FROM "get_report_02"(%s::date, %s::date, %s::int);'

        return ReportByMonthModel.objects.raw(sql_text, [self.date_start.strftime('%d.%m.%Y'),
                                                         self.date_end.strftime('%d.%m.%Y'),
                                                         self.etrap])

