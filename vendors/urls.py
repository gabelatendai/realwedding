
from django.urls import path
from vendors import views

urlpatterns = [

    path('', views.vendors, name='vendors')
    ]