from statistics import mode
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models


class listings(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, blank=True)
    bid = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.URLField()
    category = models.CharField(max_length=32, blank=True)
    date = models.DateTimeField(auto_now=True)
    seller = models.CharField(max_length=64)

class User(AbstractUser):
    watchlist = models.ManyToManyField(listings, blank=True, related_name="watchlist")
    pass

class bids(models.Model):
    pass

class comments(models.Model):
    pass

'''class watchlist(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    listings = models.ManyToManyField(listings, blank=True, related_name="listings")'''

'''class watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(listings, on_delete=models.CASCADE)
'''

'''class watchlist(models.Model):
    users = models.ManyToManyField(User, blank=True)
    listings = models.ManyToManyField(listings, blank=True, related_name="listings")'''

