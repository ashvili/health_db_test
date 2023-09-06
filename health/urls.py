from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

from health import settings

urlpatterns = [
    # path('', TemplateView.as_view(template_name='main_page/main_page.html'), name='main_page'),
    path('', include('main_page.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('patients/', include('patients.urls')),
    path('therapy/', include('therapy.urls')),
    path('surgery/', include('surgery.urls')),
    path('investment/', include('investment.urls')),
    path('dicts/', include('dicts.urls')),
    path('diagnosis/', include('diagnosis.urls')),
    path('resolution/', include('resolution.urls')),
    path('reports/', include('reports.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'^rosetta/', include('rosetta.urls')),
]
              #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
