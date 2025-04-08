from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def login_view(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('main:dashboard')
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})

