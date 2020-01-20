from django.urls import path
from .views import (
ListingCreateView
,ListingUpdateView
,ListingDeleteView
)
from . import views

urlpatterns =[

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('qoute/<int:qots_id>', views.qoutedel, name='qoutedel'),
    path('listing', views.dlisting ,name='dashboard-listing'),
    path('pricing', views.pricing, name='dashboard-pricing'),
    path('newlisting/', ListingCreateView.as_view(), name='listing-create'),
    path('listing/<int:pk>/update', ListingUpdateView.as_view(), name='listing-update'),
    path('listing/<int:pk>/delete', ListingDeleteView.as_view(), name='listing-delete'),
    #path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('qoute', views.qoute, name='qoute-request'),
    path('reviews', views.reviews, name='dashboard-reviews'),

]