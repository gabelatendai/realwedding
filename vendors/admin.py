from django.contrib import admin

from .models import Vendors


class VendorsAdmin(admin.ModelAdmin):
    list_display = ('id','user','paid','bzname','purpose')
    list_filter = ('id', 'user')
    list_display_links = ('id','user',)


admin.site.register(Vendors, VendorsAdmin)
