from django.shortcuts import render, redirect
from django.contrib.auth import login
from tienda.forms import RegistroForm
from django.contrib.auth.models import Group

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo, created = Group.objects.get_or_create(name="Cliente")
            user.groups.add(grupo)
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistroForm()
        
    return render(request, "registration/registro.html", {"form":form})


def home(request):
    return render(request, 'home.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_505(request):
    return render(request, '505.html')