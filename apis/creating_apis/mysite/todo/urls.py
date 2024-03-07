from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.ListTasks.as_view(), name="task_list"),
    path("all/", views.TaskViewSet.as_view({"get": "list"}), name="all_tasks"),
    path("<int:pk>/", views.TaskViewSet.as_view({"get": "retrieve"}), name="retrieve_task"),
]
