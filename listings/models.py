from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class Listing(models.Model):
    Category = (
        (1, 'Choose'),
        (2, 'Photographer'),
        (3, 'Florist'),
        (4, 'Cake'),
        (5, 'Catering'),
        (6, 'Clothing'),
        (7, 'Dj'),
        (8, 'Venue'),
    )
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    category = models.IntegerField(choices=Category,default=1)
    list_description = models.TextField(blank=True)
    price = models.IntegerField()
    capacity = models.IntegerField()
    longtude = models.IntegerField()
    latitude = models.IntegerField()
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    photo_main = models.ImageField(default='3.jpg',upload_to='photos/listings/')
    photo_1 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/listings/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('dashboard-listing')
