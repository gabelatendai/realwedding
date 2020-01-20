from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name',  'email','paid','bzname','purpose')
    list_filter = ('id', 'first_name')


admin.site.register(ProfileAdmin,Profile)
