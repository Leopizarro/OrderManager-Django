from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_view(request, *args, **kwargs):
    my_context = {
        "info": "info kappita desde my_context!"
    }
    return render(request, "home.html", my_context)

@login_required
def about_view(request, *args, **kwargs):
    my_context={

    }
    return render(request, "about.html", my_context)
