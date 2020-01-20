
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('listings_sidebar', views.syd, name='listings-sidebar'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
