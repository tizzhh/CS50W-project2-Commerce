from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listings/<int:listing_id>", views.listing, name="listing"),
    path("watchlist/<int:listing_id>", views.watchlist, name="watchlist"),
    path("place_bid/<int:listing_id>", views.place_bid, name="place_bid"),
    path("close_listing/<int:listing_id>", views.close_listing, name="close_listing"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category")
]
