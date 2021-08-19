from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("<slug:category_slug>/", views.store, name="prod_by_cat"),
     path("<slug:category_slug>/<slug:product_slug>/", views.prod_detail, name="product_detail")
]