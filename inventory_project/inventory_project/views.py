from .decorators import google_login_required
from django.shortcuts import render

@google_login_required(login_url='/users/')
def dashboard(request):
    return render(request, 'dashboard.html')

@google_login_required(login_url='/users/')
def about(request):
    return render(request, 'about.html')