import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings

@csrf_exempt
def login(request):
    return render(request, 'users/login.html', {
        'google_client_id': settings.GOOGLE_OAUTH_CLIENT_ID
    })

@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside')
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
    except ValueError:
        return HttpResponse(status=403)

    request.session['user_data'] = user_data
    request.session['cached_picture'] = user_data.get('picture', '')

    return redirect('dashboard')

def sign_out(request):
    del request.session['user_data']
    return redirect('users:login')