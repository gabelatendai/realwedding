
from django.urls import path
from vendors import views

urlpatterns = [

    path('', views.suppliers, name='suppliers')
    ]