from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from vendors.models import Vendors
from listings.models import Listing
from django.contrib.auth.forms import ReadOnlyPasswordHashField
User =get_user_model()

"""
class UserAdminCreationForm(forms.ModelForm):
    password1 =forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 =forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=('email',)
    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords Don't match")
        return password2
    def save(self, commit=True):
        user= super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return  user
class UserAdminChangeForm(forms.ModelForm):
    password =ReadOnlyPasswordHashField
    class Meta:
        model = User
        fields = ('email', 'password','active','admin')

        def clean_password(self):
            return self.initial['password']
"""
class VendorCreationForm(forms.ModelForm):
    class Meta:
        model= Vendors
        fields=('photo','purpose','address','phone','bzname'
        ,'description','facebook','twitter','instagram','youtube')

class ListingsForm(forms.ModelForm):
    class Meta:
        model= Listing
        fields=['title','category', 'price', 'capacity', 'list_description'
                  , 'longtude', 'latitude', 'photo_main', 'photo_1',
                  'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6'
                  , 'facebook', 'twitter', 'instagram', 'youtube']




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = get_user_model()
        fields = ("first_name","last_name","username", "email")


