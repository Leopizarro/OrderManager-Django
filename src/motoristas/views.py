from django.shortcuts import render
from .forms import RawMotoristaForm
from .models import Motorista
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_motorista_view(request):
    my_form = RawMotoristaForm
    if request.method == "POST":
        my_form = RawMotoristaForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Motorista.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "motoristas/motorista_create.html", context)
    

@login_required
def motorista_list_view(request):
    motorista_list = Motorista.objects.all()
    context = {
        'motorista_list':motorista_list
    }


    return render(request, "motoristas/motorista_list.html", context)