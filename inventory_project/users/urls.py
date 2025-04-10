from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.login, name='login'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
]