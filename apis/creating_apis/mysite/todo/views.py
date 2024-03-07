from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from .serializers import TaskSerializer
from .models import Task
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404


# class ListTasks(APIView):

#     # 1. List all tasks
#     def get(self, request, *args, **kwargs):
#         """List all todo items."""
#         # getting a list of all tasks
#         tasks = Task.objects.filter(completed=False)
#         # feed all tasks into serializer
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     # 2. Create a task
#     def post(self, request, *args, **kwargs):
#         """Create a todo with the given payload."""
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListTasks(ListCreateAPIView):
    queryset = Task.objects.filter(completed=False)
    serializer_class = TaskSerializer


class TaskViewSet(ViewSet):

    def list(self, request):
        """Listing all the task objects."""
        queryset = Task.objects.filter(completed=False)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Get a particular object."""
        queryset = Task.objects.filter(completed=False)
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    