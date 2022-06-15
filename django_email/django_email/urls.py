from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
