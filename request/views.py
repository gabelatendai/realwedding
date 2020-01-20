from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages
from django.core.mail import send_mail
from . models import Request

def request(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['comments']
        wedding_date = request.POST['weddingdate']
        user_id = request.POST['user_id']
        #supplier_email = request.POST['realtor_email']

        has_contacted =Request.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_contacted:
                messages.error(request, 'You have already made an iquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Request(listing= listing, listing_id=listing_id,name=name,email=email, phone=phone,
                          message=message,wedding_date=wedding_date,user_id=user_id)
        contact.save()

        '''send_mail(
                    'Property Listing Form',
                    'There has been an inquiry for '+ listing + '. Sign into the admin for more infor',
                    'gabrielmusodza@gmail.com',
                    [realtor_email, 'gabela.musodza33@gmail.com'],
                    fail_silently=False
                )
        '''
        messages.success(request, 'Your request has submitted, a realtor will get back to you soon ')
        return redirect('/listings/' + listing_id)
