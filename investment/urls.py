from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import InvestmentListView, InvestmentCreateView, InvestmentEditView

app_name = 'investment'

urlpatterns = [
    path('list/', login_required(InvestmentListView.as_view()), name='investment_list'),
    path('list_period/<str:date_start>/<str:date_end>/',
         login_required(InvestmentListView.as_view()), name='investment_list_period'),
    path('create/', login_required(InvestmentCreateView.as_view()), name='create'),
    path('edit/<int:pk>/', login_required(InvestmentEditView.as_view()), name='investment_edit'),
]