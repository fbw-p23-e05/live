"""ToDo URL Configuration."""
from django.urls import path

from todo import views

app_name = "todo"
urlpatterns = [
    path('<int:todo_id>/', views.details, name="details"),
]
