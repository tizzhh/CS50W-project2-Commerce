from django.contrib import admin
from .models import listings, User, bids, comments

# Register your models here.
admin.site.register(listings)
admin.site.register(User)
admin.site.register(bids)
admin.site.register(comments)