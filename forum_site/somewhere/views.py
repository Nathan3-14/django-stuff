from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from forum_site.settings import STATICFILES_DIRS
from somewhere.models import NameForm

def index(request):
    context = {}

    return render(request, "somewhere/index.html", context)


