from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/users/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/users/login/')
def about(request):
    return render(request, 'about.html')