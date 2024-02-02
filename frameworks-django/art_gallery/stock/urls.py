from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.listings, name="listings"),
    path("item/<int:item_id>/", views.search_item, name="search_item"),
    path("item/<str:item_name>/", views.search_item_by_key, name="search_by_key"),
]
