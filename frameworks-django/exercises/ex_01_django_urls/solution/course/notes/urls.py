"""Notes URL Configuration."""
from django.urls import path

from notes import views

app_name = "notes"
urlpatterns = [
    path('', views.home, name="home"),
    path('sections/', views.sections, name="sections"),
    path('sections/<section_name>/', views.by_section, name="by_section"),
    path('<int:note_id>/', views.details, name="details"),
    path('<str:search_term>/', views.search, name="search"),
]
