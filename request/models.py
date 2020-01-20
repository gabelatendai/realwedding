from django.db import models
from datetime import datetime


class Request(models.Model):
    listing = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    listing_id= models.IntegerField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id =models.IntegerField(blank=True)
    wedding_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

