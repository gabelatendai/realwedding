from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
   # user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
   # user_id = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bzname = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    description = models.TextField(blank=True)
    purpose = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    facebook = models.CharField(max_length=200,blank=True)
    twitter = models.CharField(max_length=200,blank=True)
    instagram = models.CharField(max_length=200,blank=True)
    youtube = models.CharField(max_length=200,blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
