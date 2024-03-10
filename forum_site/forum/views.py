from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post, PostForm

def index(request):
    latest_post_list = Post.objects.order_by("-post_pub_date")[:5]
    context = {
        "latest_post_list": latest_post_list
    }
    return render(request, "forum/index.html", context)


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "forum/post.html", {"post": post})

def make_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = PostForm()
    
    return render(request, "forum/name.html", {"form": form})

