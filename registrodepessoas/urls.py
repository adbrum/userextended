from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from registrodepessoas.core.views import register

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^registrar/$', register, name='register'),
    url(r'^admin/', include(admin.site.urls)),
]
