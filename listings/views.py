from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from  vendors.models import Vendors
from django.contrib.auth.models import User
from .choices import price_choices, vendor_choices,guest_capacity


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)  # Show 6 contacts per page

    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
         'listings': page_listings
    }
    return render(request, 'listings/listings.html', context)

def syd(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 4)  # Show 6 contacts per page

    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
         'listings': page_listings
    }
    return render(request, 'listings/listings_sydbar.html', context)
def listing(request, listing_id):
    listings = get_object_or_404(Listing, pk=listing_id)
    vendor = Vendors.objects.get(user=listings.user)


    context = {
        'listings': listings,
        'vendor': vendor,

    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # city
    if 'category' in request.GET:
       category = request.GET['category']
       if category:
          queryset_list = queryset_list.filter(category__iexact=category)
    # capacity

    if 'capacity' in request.GET:
        capacity = request.GET['capacity']
        if capacity:
            queryset_list = queryset_list.filter(capacity__lte=capacity)
          # price
    if 'price' in request.GET:
         price = request.GET['price']
         if price:
              queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'vendor_choices': vendor_choices,
        'price_choices': price_choices,
        'guest_capacity': guest_capacity,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
