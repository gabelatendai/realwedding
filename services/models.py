from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #user =models.IntegerField()
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=20)
    capacity = models.IntegerField()
    longtude = models.IntegerField(blank=True)
    latitude = models.IntegerField(blank=True)
    facebook = models.CharField(max_length=200,blank=True)
    twitter = models.CharField(max_length=200,blank=True)
    instagram = models.CharField(max_length=200,blank=True)
    youtube = models.CharField(max_length=200,blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
