from django.shortcuts import render
from listings.models import Listing
from  vendors.models import Vendors

from services.choices import vendor_choices,city_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    venues = Listing.objects.order_by('-list_date').filter(category=8)

    context = {
        'vendor_choices': vendor_choices,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,

    }
    return render(request, 'pages/index.html',context)


def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    vendors = Vendors.objects.order_by('-reg_date').filter(paid=True)
    venues = Listing.objects.order_by('-list_date').filter(category=8)
    photo = Listing.objects.order_by('-list_date').filter(category=2)
    florist = Listing.objects.order_by('-list_date').filter(category=3)
    clothing = Listing.objects.order_by('-list_date').filter(category=6)
    dj = Listing.objects.order_by('-list_date').filter(category=7)
    cake= Listing.objects.order_by('-list_date').filter(category=4)

    context = {
        'vendor_choices': vendor_choices,
        'vendors': vendors,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,
        'florist': florist,
        'photo': photo,
        'clothing': clothing,
        'dj': dj,
        'cake': cake,
    }
    return render(request, 'pages/home.html',context)

def clothing(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    vendors = Vendors.objects.order_by('-reg_date').filter(paid=True)
    venues = Listing.objects.order_by('-list_date').filter(category=8)
    photo = Listing.objects.order_by('-list_date').filter(category=2)
    florist = Listing.objects.order_by('-list_date').filter(category=3)
    clothing = Listing.objects.order_by('-list_date').filter(category=6)
    dj = Listing.objects.order_by('-list_date').filter(category=7)
    cake= Listing.objects.order_by('-list_date').filter(category=4)

    context = {
        'vendor_choices': vendor_choices,
        'vendors': vendors,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,
        'florist': florist,
        'photo': photo,
        'clothing': clothing,
        'dj': dj,
        'cake': cake,
    }
    return render(request, 'pages/dresses.html',context)
def venues(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    vendors = Vendors.objects.order_by('-reg_date').filter(paid=True)
    venues = Listing.objects.order_by('-list_date').filter(category=8)
    photo = Listing.objects.order_by('-list_date').filter(category=2)
    florist = Listing.objects.order_by('-list_date').filter(category=3)
    clothing = Listing.objects.order_by('-list_date').filter(category=6)
    dj = Listing.objects.order_by('-list_date').filter(category=7)
    cake= Listing.objects.order_by('-list_date').filter(category=4)

    context = {
        'vendor_choices': vendor_choices,
        'vendors': vendors,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,
        'florist': florist,
        'photo': photo,
        'clothing': clothing,
        'dj': dj,
        'cake': cake,
    }
    return render(request, 'pages/venues.html',context)
def cakes(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    vendors = Vendors.objects.order_by('-reg_date').filter(paid=True)
    venues = Listing.objects.order_by('-list_date').filter(category=8)
    photo = Listing.objects.order_by('-list_date').filter(category=2)
    florist = Listing.objects.order_by('-list_date').filter(category=3)
    clothing = Listing.objects.order_by('-list_date').filter(category=6)
    dj = Listing.objects.order_by('-list_date').filter(category=7)
    cake= Listing.objects.order_by('-list_date').filter(category=4)

    context = {
        'vendor_choices': vendor_choices,
        'vendors': vendors,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,
        'florist': florist,
        'photo': photo,
        'clothing': clothing,
        'dj': dj,
        'cake': cake,
    }
    return render(request, 'pages/cakes.html',context)
def florist(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    vendors = Vendors.objects.order_by('-reg_date').filter(paid=True)
    venues = Listing.objects.order_by('-list_date').filter(category=8)
    photo = Listing.objects.order_by('-list_date').filter(category=2)
    florist = Listing.objects.order_by('-list_date').filter(category=3)
    clothing = Listing.objects.order_by('-list_date').filter(category=6)
    dj = Listing.objects.order_by('-list_date').filter(category=7)
    cake= Listing.objects.order_by('-list_date').filter(category=4)

    context = {
        'vendor_choices': vendor_choices,
        'vendors': vendors,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,
        'florist': florist,
        'photo': photo,
        'clothing': clothing,
        'dj': dj,
        'cake': cake,
    }
    return render(request, 'pages/florist.html',context)
def catering(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    vendors = Vendors.objects.order_by('-reg_date').filter(paid=True)
    venues = Listing.objects.order_by('-list_date').filter(category=8)
    photo = Listing.objects.order_by('-list_date').filter(category=2)
    florist = Listing.objects.order_by('-list_date').filter(category=3)
    clothing = Listing.objects.order_by('-list_date').filter(category=6)
    dj = Listing.objects.order_by('-list_date').filter(category=7)
    cake= Listing.objects.order_by('-list_date').filter(category=4)
    catering= Listing.objects.order_by('-list_date').filter(category=5)

    context = {
        'vendor_choices': vendor_choices,
        'vendors': vendors,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,
        'florist': florist,
        'photo': photo,
        'clothing': clothing,
        'dj': dj,
        'cake': cake,
        'catering': catering,
    }
    return render(request, 'pages/catering.html',context)
def camera(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    vendors = Vendors.objects.order_by('-reg_date').filter(paid=True)
    venues = Listing.objects.order_by('-list_date').filter(category=8)
    photo = Listing.objects.order_by('-list_date').filter(category=2)
    florist = Listing.objects.order_by('-list_date').filter(category=3)
    clothing = Listing.objects.order_by('-list_date').filter(category=6)
    dj = Listing.objects.order_by('-list_date').filter(category=7)
    cake= Listing.objects.order_by('-list_date').filter(category=4)

    context = {
        'vendor_choices': vendor_choices,
        'vendors': vendors,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,
        'florist': florist,
        'photo': photo,
        'clothing': clothing,
        'dj': dj,
        'cake': cake,
    }
    return render(request, 'pages/photographer.html',context)
def dj(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    vendors = Vendors.objects.order_by('-reg_date').filter(paid=True)
    venues = Listing.objects.order_by('-list_date').filter(category=8)
    photo = Listing.objects.order_by('-list_date').filter(category=2)
    florist = Listing.objects.order_by('-list_date').filter(category=3)
    clothing = Listing.objects.order_by('-list_date').filter(category=6)
    dj = Listing.objects.order_by('-list_date').filter(category=7)
    cake= Listing.objects.order_by('-list_date').filter(category=4)

    context = {
        'vendor_choices': vendor_choices,
        'vendors': vendors,
        'city_choices': city_choices,
        'listings': listings,
        'venues': venues,
        'florist': florist,
        'photo': photo,
        'clothing': clothing,
        'dj': dj,
        'cake': cake,
    }
    return render(request, 'pages/dj.html',context)

#def vendors(request):
 #   return render(request, 'pages/vendors.html')


def about(request):
    return render(request, 'pages/about.html')
def team(request):
    return render(request, 'pages/team.html')
def pricing(request):
    return render(request, 'pages/pricing.html')

"""def signup(request):
    if request.method == 'POST':
         form = SignUpForm(request.POST)
         if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})"""