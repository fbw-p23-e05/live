from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.ListTasks.as_view(), name="task_list"),
    path("all/", views.TaskViewSet.as_view({"get": "list"}), name="all_tasks"),
    path("<int:pk>/", views.TaskViewSet.as_view({"get": "retrieve"}), name="retrieve_task"),
    path('authtoken/', obtain_auth_token, name="api_auth_token"),
]
