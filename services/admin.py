from django.contrib import admin

from .models import Service


class ListingAd(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'user','capacity','category')
    list_display_links = ('id', 'title')
    list_filter = ('user',)
    list_editable = ('is_published',)
    search_fields = ('description', 'title', 'price', 'address', 'zipcode', 'city', 'state')
    list_per_page = 25

admin.site.register(Service, ListingAd)
