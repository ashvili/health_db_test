import datetime

from django.utils.dateparse import parse_date
from django.utils.timezone import now
from django_currentuser.middleware import get_current_authenticated_user


DATA_LANGUAGE_CODE = 'tk'

def set_data_lang():
    global DATA_LANGUAGE_CODE
    current_user = get_current_authenticated_user()
    if not current_user is None:
        if current_user.data_lang == 0:
            DATA_LANGUAGE_CODE = 'en'
        elif current_user.data_lang == 1:
            DATA_LANGUAGE_CODE = 'ru'
        else:
            DATA_LANGUAGE_CODE = 'tk'
    else:
        DATA_LANGUAGE_CODE = 'tk'

def get_data_lang():
    current_user = get_current_authenticated_user()
    if not current_user is None:
        if current_user.data_lang == 0:
            return 'en'
        elif current_user.data_lang == 1:
            return 'ru'
    return 'tk'

class SearchViewMixin:
    def init_params(self):
        self.date_start = self.kwargs.get('date_start', '') if self.kwargs.get('date_start', '') != '' \
            else datetime.date(now().year, now().month, 1)
        self.date_end = self.kwargs.get('date_end', '') if self.kwargs.get('date_end') != '' \
            else datetime.date(now().year, now().month, 1) + relativedelta(months=1)
        self.etrap = self.kwargs.get('etrap', -1)
        if isinstance(self.date_start, str):
            self.date_start = parse_date(self.date_start)
        if isinstance(self.date_end, str):
            self.date_end = parse_date(self.date_end)
        if isinstance(self.etrap, str):
            self.etrap = int(self.etrap)
