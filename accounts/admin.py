"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email','admin',)
    list_filter = ('admin','active','staff',)
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Personal Info',{'fields':('',)}),
        ('Permisions',{'fields':('admin','staff','active',)}),
    )
    add_fields=(
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2',)}
         ),
    )
    search_fields = ['email',]
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# Register your models here.

"""