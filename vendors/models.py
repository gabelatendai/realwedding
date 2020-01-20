from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#from accounts.models import User
#User= settings.AUTH_USER_MODEL

class Vendors(models.Model):

    Purposes = (
        (1, 'Choose'),
        (2, 'Photographer'),
        (3, 'Florist'),
        (4, 'Cake'),
        (5, 'Catering'),
        (6, 'Clothing'),
        (7, 'Dj'),
        (8, 'Venue'),
    )
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    bzname = models.CharField(max_length=200)
    photo = models.ImageField(default='default.png', upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    purpose = models.IntegerField(choices=Purposes,default=1)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    facebook = models.CharField(max_length=200,blank=True)
    twitter = models.CharField(max_length=200,blank=True)
    instagram = models.CharField(max_length=200,blank=True)
    youtube = models.CharField(max_length=200,blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)


User.vendors= property(lambda u: Vendors.objects.get_or_create(user=u)[0])