from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogPostSerializer
from .models import BlogPost


class PostListView(ListCreateAPIView):
    """Get a list of all posts
    Create new posts.
    """
    permission_classes = [DjangoModelPermissions]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    
# class PostDetailView(RetrieveUpdateAPIView):
#     """Retrieve a specific post.
#     Update that post.
#     """
#     permission_classes = [DjangoModelPermissions]
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer    

class PostDetailView(APIView):

    def __get_object(self, post_id):
        """
        Helper method to get a specific object.
        """
        try:
            return BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            return None

    def get(self, request, post_id, *args, **kwargs):
        """Retrieves a specific blog post."""
        blog_post = self.__get_object(post_id)

        if not blog_post:
            message = {"response": f"Blog post with ID #{post_id} does not exist."}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        # if blog post exists create a serializer object
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, post_id, *args, **kwargs):
        """
        Update a blog post.
        """
        blog_post = self.__get_object(post_id)
        if not blog_post:
            message = {"response": f"Blog post with ID #{post_id} does not exist."}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        serializer = BlogPostSerializer(instance=blog_post, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, post_id, *args, **kwargs):
        """Deletes an object given the todo_id"""
        # Retrieve object
        blog_post = self.get_object(post_id)
        if not blog_post:
            return Response({"response": f"Object with ID #{post_id} does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)
            
        # Delete object if it it exists
        blog_post.delete()
        return Response({"message": "Object successfully deleted!"}, status=status.HTTP_204_NO_CONTENT)
