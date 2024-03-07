from django.shortcuts import get_object_or_404, render

def index(request):

    context = {
        "pages": [
            "/forum",
            "/somewhere"
        ]
    }
    
    return render(request, "index/index.html", context)