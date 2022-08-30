from django.contrib import admin
from .models import listings, User

# Register your models here.
admin.site.register(listings)
admin.site.register(User)