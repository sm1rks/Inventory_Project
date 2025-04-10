from django.shortcuts import redirect
from functools import wraps

def google_login_required(login_url='/users/login'):
    """
    Decorator to require the user to be logged in via Google.
    If the user is not logged in, they are redirected to the login URL.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if 'user_data' not in request.session:
                return redirect(login_url)  # Redirect to the provided login URL if not authenticated via Google
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
