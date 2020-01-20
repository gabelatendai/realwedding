from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Vendors




def vendors(request):

    photography = Vendors.objects.filter(purpose=2)
    florist = Vendors.objects.filter(purpose=3)
    cakes = Vendors.objects.filter(purpose=4)
    catering = Vendors.objects.filter(purpose=5)
    clothing = Vendors.objects.filter(purpose=6)
    dj = Vendors.objects.filter(purpose=7)
    venue = Vendors.objects.filter(purpose=8)

    context = {
       'venue' : venue,
       'clothing' : clothing,
       'photography' : photography,
       'cakes' : cakes,
       'catering' : catering,
       'dj' : dj,
       'florist' : florist,
    }
    return render(request, 'pages/vendors.html',context)


