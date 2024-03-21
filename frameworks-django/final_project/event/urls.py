from django.urls import path
from . import api_views

app_name = 'event'

urlpatterns = [
    path('events/', api_views.EventListCreate.as_view(), name='event-list-create'),
    path('events/<int:pk>/', api_views.EventRetrieveUpdateDestroy.as_view(), name='event-retrieve-update-destroy'),
]