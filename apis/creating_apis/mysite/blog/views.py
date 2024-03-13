from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from .serializers import BlogPostSerializer
from .models import BlogPost


class PostListView(ListCreateAPIView):
    """Get a list of all posts
    Create new posts.
    """
    permission_classes = [DjangoModelPermissions]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    
class PostDetailView(RetrieveUpdateAPIView):
    """Retrieve a specific post.
    Update that post.
    """
    permission_classes = [DjangoModelPermissions]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer    
