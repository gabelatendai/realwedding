
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('pricing', views.pricing, name='pricing'),
    path('dresses', views.clothing, name='clothing'),
    path('cakes', views.cakes, name='cakes'),
    path('dj', views.dj, name='dj'),
    path('catering', views.catering, name='catering'),
    path('venues', views.venues, name='venues'),
    path('florist', views.florist, name='florist'),
    path('photographers', views.camera, name='photographers'),

]
