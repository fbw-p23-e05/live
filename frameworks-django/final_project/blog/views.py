from django.shortcuts import render, redirect
from .models import Post

from django.db.models import Q

from .forms import SearchForm, PostForm

from django.contrib.auth.decorators import login_required

# Create your views here.

# def post_list(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'blog/post_list.html', {'posts': posts})



def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    form = SearchForm()
    key = request.GET.get('keyword')

    if key:
        posts = posts.filter(Q(content__icontains = key) | Q(title__icontains = key))

    return render(request, 'blog/post_list.html', {'posts': posts, 'form': form})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('blog:post_list')  # Redirect to post list page after successful form submission
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})



def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})



# def post_search(request):

#     content_q = request.GET.get('content_q')
#     # title_q = request.GET.get('title_q')

#     posts = Post.objects.all()

#     if content_q:
#         # posts = posts.filter(content__icontains = content_q)

#         posts = posts.filter(Q(content__icontains = content_q) | Q(title__icontains = content_q))

#     # if title_q:
#     #     posts = posts.filter(title__icontains = title_q)

#     return render(request, 'blog/post_search.html', {'posts': posts})



def post_search(request):

    content_q = request.GET.get('content_q')
    title_q = request.GET.get('title_q')

    posts = Post.objects.all()

    if content_q:
        posts = posts.filter(Q(content__icontains = content_q) | Q(title__icontains = content_q))

    if title_q:
        posts = posts.filter(title__icontains = title_q)

    return render(request, 'blog/post_search.html', {'posts': posts})