import datetime
from django.http import HttpResponse
from django.shortcuts import reverse, render, get_object_or_404
from django.views.generic import View
from .models import Post
from .forms import CommentForm
# Login required decorator
from django.contrib.auth.decorators import login_required


def home(request):
    text = "Welcome to the PythonBugs Blog"
    posts = Post.objects.all()
    
    return render(request, 'blog/index.html', {"welcome_text": text,
                                               "all_posts": posts})
    

@login_required
def post_detail(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)
    comments = blog_post.comments.filter(active=True)
    
    new_comment = None
    
    if request.method == "POST":
        # A comment was passed
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create the comment but dont save
            new_comment = comment_form.save(commit=False)
            # Assign post to the form
            new_comment.post = blog_post
            # Save the comment
            new_comment.save()
    else:
        # For GET request.
        comment_form = CommentForm()
    
    return render(request, 'blog/post-detail.html',
                  {"post": blog_post, "comments": comments,
                   "new_comment": new_comment, "comment_form": comment_form})

