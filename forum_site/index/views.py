from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! You are at the index for the site")