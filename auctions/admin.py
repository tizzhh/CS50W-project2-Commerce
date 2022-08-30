from django.contrib import admin
from .models import listings, watchlist

# Register your models here.
admin.site.register(listings)
admin.site.register(watchlist)