import datetime

from dateutil.relativedelta import relativedelta
from django.db.models import Count, Sum
from django.utils.timezone import now
from django.views.generic import TemplateView

from diagnosis.models import PatientDiagnosis
from health import settings
from investment.models import Investment
from reports.models import PatientEvent
from reports.views import ReportInfoView
from surgery.models import PatientSurgery
from therapy.models import PatientTherapy


class MainPageView(TemplateView):
    template_name = 'main_page/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['start_year'] = f'{now().year}-1-1'
        context['end_year'] = f'{now().year}-12-31'

        context['start_month'] = f'{now().year}-{now().month}-1'
        context['end_month'] = datetime.datetime.strftime(
            datetime.date(now().year, now().month, 1) + relativedelta(months=1), '%Y-%m-%d')



        context['surgery_total'] = PatientSurgery.objects\
                                                 .aggregate(count=Count('id'), sum=Sum('price_man'))
        context['surgery_year'] = PatientSurgery.objects\
                                                .filter(surgery_date__year=now().year)\
                                                .aggregate(count=Count('id'), sum=Sum('price_man'))
        context['therapy_total'] = PatientTherapy.objects\
                                                 .aggregate(count=Count('id'), sum=Sum('price_man'))
        context['therapy_year'] = PatientTherapy.objects\
                                                .filter(exit_date__year=now().year)\
                                                .aggregate(count=Count('id'), sum=Sum('price_man'))
        context['diagnosis_total'] = PatientDiagnosis.objects\
                                                     .aggregate(count=Count('id'), sum=Sum('price_man'))
        context['diagnosis_year'] = PatientDiagnosis.objects\
                                                    .filter(exit_date__year=now().year)\
                                                    .aggregate(count=Count('id'), sum=Sum('price_man'))
        context['investment_total'] = Investment.objects\
                                                .aggregate(count=Count('id'), sum=Sum('price_man'))
        context['investment_year'] = Investment.objects\
                                               .filter(investment_date__year=now().year)\
                                               .aggregate(count=Count('id'), sum=Sum('price_man'))
        context['patient_events'] = PatientEvent.objects.all()[:settings.LIST_PAGE_SIZE]
        return context
