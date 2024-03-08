from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from forum_site.settings import STATICFILES_DIRS
from somewhere.models import NameForm

def index(request):
    context = {}

    return render(request, "somewhere/index.html", context)

def name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            dir = f"{STATICFILES_DIRS[2]}/test.txt"
            with open(dir, "w") as f:
                f.write(f"{form.cleaned_data["name"]}\n  Have written!")
            
            return HttpResponseRedirect("/")
    else:
        form = NameForm()
    
    return render(request, "somewhere/name.html", {"form": form})
