from django import forms
from django.dispatch import receiver
from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
from django.views.generic import (CreateView,UpdateView,DeleteView)
from listings.models import Listing
from vendors.models import Vendors
from vendors.signals import User
from request.models import Request
#from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.signals import post_save
from .forms import (
    VendorCreationForm, ListingsForm,UserUpdateForm)
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

       if password == password2:
           if User.objects.filter(username=username).exists():
               messages.error(request, 'Username Taken')
               return redirect('register')
           else:
               if User.objects.filter(email=email).exists():
                   messages.error(request, 'Email is Taken by another user')
                   return redirect('register')
               else:
                   user = User.objects.create_user(username=username, password=password, email=email,
                                                   first_name=first_name, last_name=last_name)
                   #auth.login(request,user)
                   #messages.error(request, 'You are logged in')
                   #return redirect('index')
           user.save()
           messages.error(request, 'You now registered')
           return redirect('login')
       else:
          messages.error(request, 'Passwords do not match')
          return redirect('register')
    else:
        return render(request,'accounts/register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def dashboard(request):
    user_listings = Listing.objects.order_by('-list_date').filter(user=request.user.id)
    if request.user.is_authenticated:
        user_id = request.user.id
        user_profile = Vendors.objects.get(user_id=user_id)
        quote = Request.objects.filter(user_id=user_profile.id)
        context = {
            'quote': quote,
            'listings': user_listings,
        }

        return render(request,'accounts/dashboard.html',context)
def userprofile(request):
    if request.user.is_authenticated:
        user_id = request.user.id

        return render(request,'accounts/vendo_profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = VendorCreationForm(request.POST,request.FILES, instance=request.user.vendors)
        userform = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid() and userform.is_valid():
            form.save()
            userform.save()
            messages.success(request, 'Profile Updated Successfully ')
            return HttpResponseRedirect('dashboard')
    else:
        form = VendorCreationForm(instance=request.user.vendors)
        userform = UserUpdateForm(instance=request.user)
        context={
            'form':form,
            'userform':userform
        }

        return render(request, 'accounts/vendo_profile.html',  context)

@login_required
def newlistings(request):
    if request.method == 'POST':
        form = ListingsForm(request.POST, request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
        messages.success(request, 'Listing  Successfully Added ')
        return HttpResponseRedirect('dashboard')
    else:
        form = ListingsForm(instance=request.user)
        return render(request, 'accounts/dashboard-add-listing.html', {'form': form})

class ListingCreateView(LoginRequiredMixin,CreateView):
    model = Listing
    fields=['title','category', 'price', 'capacity', 'list_description'
                  , 'longtude', 'latitude', 'photo_main', 'photo_1',
                  'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6'
                  , 'facebook', 'twitter', 'instagram', 'youtube']
    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)

class ListingUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Listing
    fields=['title','category', 'price', 'capacity', 'list_description'
                  , 'longtude', 'latitude', 'photo_main', 'photo_1',
                  'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6'
                  , 'facebook', 'twitter', 'instagram', 'youtube']
    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)

    def test_func(self):
        listing = self.get_object()
        if self.request.user==listing.user:
            return True
        return False
class ListingDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Listing
    success_url = '/accounts/listing'

    def test_func(self):
        listing = self.get_object()
        if self.request.user==listing.user:
            return True
        return False



def dlisting(request):
    user_listings = Listing.objects.order_by('-list_date').filter(user=request.user.id)
    if request.user.is_authenticated:
        user_id = request.user.id
        user_profile = Vendors.objects.get(user_id=user_id)
        context = {
            'listings': user_listings,
        }
        return render(request, 'accounts/dashboard-listing.html',context)

def add_listing(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_profile = Vendors.objects.get(user_id=user_id)
        quote = Request.objects.filter(user_id=user_profile.id)
        context = {
            'quote': quote,
            'profile': user_profile,
        }
        return render(request, 'accounts/dashboard-add-listing.html',context)

def qoute(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_profile = Vendors.objects.get(user_id=user_id)
        quote = Request.objects.filter(user_id=user_profile.id)
        context = {
            'quote': quote,
            'profile': user_profile,
        }
        return render(request, 'accounts/dashboard-qoute-request.html',context)
def qoutedel(request, qots_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        quote = Request.objects.get(pk=qots_id,user_id=user_id)
        quote.delete()
        messages.error(request, 'Successfully deleted')
    
        return render(request, 'accounts/dashboard-qoute-request.html')


def pricing(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_profile = Vendors.objects.get(user_id=user_id)
        context = {
            'profile': user_profile,
        }
        return render(request, 'accounts/dashboard-pricing.html',context)


def reviews(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_profile = Vendors.objects.get(user_id=user_id)
        context = {
            'profile': user_profile,
        }
        return render(request, 'accounts/dashboard-reviews.html',context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You logged out')
        return redirect('index')
