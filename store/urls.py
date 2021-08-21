from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("search/", views.search, name="search"),
    path("category/<slug:category_slug>/", views.store, name="prod_by_cat"),
    path("category/<slug:category_slug>/<slug:product_slug>/", views.prod_detail, name="product_detail"),
]