from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import MainPageView


app_name = 'main_page'

urlpatterns = [
    path('', login_required(MainPageView.as_view()), name='main_page'),
]