from django.http import HttpResponseRedirect
from django.shortcuts import render

from somewhere.models import NameForm

def name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect("/")
    else:
        form = NameForm()
    
    return render(request, "forum/post_create.html", {"form": form})

def index(request):
    context = {}

    return render(request, "testing/index.html", context)
