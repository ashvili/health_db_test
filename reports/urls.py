from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from .views import ReportPageView, SearchStatisticView, SearchStatisticByVelayatView, SearchHospitalsView, \
    SearchStatisticByMonthView

app_name = 'reports'

urlpatterns = [
    path('', login_required(ReportPageView.as_view()), name='reports'),
    re_path('statistic/(?P<date_start>[^/]+)/(?P<date_end>[^/]+)/(?P<etrap>[-]?[0-9]+)/\\Z',
            login_required(SearchStatisticView.as_view()), name='report_statistic'),
    re_path('statistic_by_velayat/(?P<date_start>[^/]+)/(?P<date_end>[^/]+)$',
            login_required(SearchStatisticByVelayatView.as_view()), name='statistic_by_velayat'),
    re_path('statistic_by_month/(?P<date_start>[^/]+)/(?P<date_end>[^/]+)/(?P<etrap>[-]?[0-9]+)/\\Z',
            login_required(SearchStatisticByMonthView.as_view()), name='statistic_by_month'),
    re_path('hospitals/(?P<date_start>[^/]+)/(?P<date_end>[^/]+)$',
            login_required(SearchHospitalsView.as_view()), name='hospitals'),
]