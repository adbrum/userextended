from django.conf.urls import url
from django.contrib import admin
from registrodepessoas.core.views import register

urlpatterns = [
    url(r'^$', register, name='register'),
    url(r'^admin/', admin.site.urls),
]
