from django.contrib import admin
from . models import Request


class ContactsAdmin (admin.ModelAdmin):
    list_display = ('id','name', 'listing', 'email', 'contact_date','wedding_date','user_id')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Request, ContactsAdmin)