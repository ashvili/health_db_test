import datetime

from dateutil.relativedelta import relativedelta
from django import forms
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from crispy_forms.bootstrap import FormActions, TabHolder, Tab, InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, Div, Field, Hidden, HTML
from django.urls import reverse
from easy_select2 import Select2

from dicts.models import Etrap
from health import settings


class ReportParametersForm(forms.Form):
    date_start = forms.DateField(
                                    widget=forms.DateInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                    required=False, label=_('Начало'),
                                    # default=datetime.date(now().year, now().month, 1),
                                   )
    date_end = forms.DateField(
                                    widget=forms.DateInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
                                    required=False, label=_('Конец'),
                                    # default=datetime.date(now().year, now().month, 1) + relativedelta(months=1),
                                   )

    etrap = forms.ModelChoiceField(queryset=Etrap.objects.all(), initial=None,
                                  required=False, label=_('Велаят/город'),
                                  widget=Select2(select2attrs={'width': '100%'}))

    date_period = forms.ChoiceField(choices=settings.PERIODS,
                                    required=False,
                                    label=_('Период'),
                                    widget=forms.Select(attrs={'onchange': 'setDates()'}))

    class Meta:
        fields = [
            'date_start', 'date_end', 'etrap',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div('date_period', css_class='col-3', ),
                        Div('date_start', css_class='col-3', ),
                        Div('date_end', css_class='col-3', ),
                        Div('etrap', css_class='col-3', ),
                        css_class='row'
                    ),
                    css_class=' ',
                ),
                css_class='col-10',
            ),
            Div(
                HTML('<button type="submit" class="btn btn-link" name="statistic" id="id_report_statistic1">%s</button>' % _('Статистика за период')),
                HTML('<button type="submit" class="btn btn-link" name="statistic_by_velayat" id="id_report_statistic_by_velayat">%s</button>' % _(
                    'Статистика по велаятам')),
                HTML('<button type="submit" class="btn btn-link" name="statistic_by_month" id="id_report_statistic_by_month">%s</button>' % _(
                    'Статистика по месяцам')),
                HTML('<button type="submit" class="btn btn-link" name="hospitals" id="id_report_hospitals">%s</button>' % _(
                    'Суммы по больницам')),
                css_class='',
            ),
            Div(
                css_class='',
            ),

        )



