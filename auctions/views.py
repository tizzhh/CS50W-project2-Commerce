from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import User, listings, bids, comments


def index(request):
    return render(request, "auctions/index.html", {
        "listings": listings.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class NewTaskForm(forms.Form):
    name = forms.CharField(label="Listing name")
    description = forms.CharField(label="Description", required=False)
    bid = forms.DecimalField(label="Starting bid", max_digits=100, decimal_places=2)
    image = forms.URLField(label="Photo URL", required=False)
    category = forms.CharField(label="Category", required=False)

@login_required
def create_listing(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        bid = request.POST["bid"]
        image = request.POST["image"]
        seller = request.user
        listings.objects.create(name=name, description=description, bid=bid, image=image, seller=seller)
        return HttpResponseRedirect(reverse("index"))
        
        
    return render(request, "auctions/create_listing.html", {
        "form": NewTaskForm()
    })


def listing(request, listing_id):
    listing = listings.objects.get(id=listing_id)
    # https://stackoverflow.com/questions/16181188/django-doesnotexist
    try:
        watchlist = request.user.watchlist.get(id=listing_id)
    except ObjectDoesNotExist:
        watchlist = None
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "watchlist": watchlist
    })

@login_required
def watchlist(request):
    # https://stackoverflow.com/questions/26048602/how-do-i-get-the-name-of-a-form-after-a-post-request-in-django
    print(request.POST)
    if request.method == "POST" and "add" in request.POST:
        request.user.watchlist.add(listings.objects.get(id=request.POST["id"]))
    if request.method == "POST" and "remove" in request.POST:
        request.user.watchlist.remove(listings.objects.get(id=request.POST["id"]))
    return render(request, "auctions/watchlist.html", {
        "listings": request.user.watchlist.all()
    })