import datetime
from time import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from forum_site.settings import STATICFILES_DIRS

from .models import Post, PostForm

import json

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
            file_path = f"{STATICFILES_DIRS[2]}/posts.json"

            current_data = json.load(open(file_path, "r"))
            current_data[form.cleaned_data["post_title"]] = "Coolio!"

            json.dump(current_data, open(file_path, "w"))

            form.instance.post_pub_date = datetime.datetime.now()
            form.save()
            
            return HttpResponseRedirect("/forum")
    else:
        form = PostForm()
    
    return render(request, "forum/post_create.html", {"form": form})

