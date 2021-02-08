from django.shortcuts import render
from django.contrib.auth import login, logout
from accounts.models import authenticate 
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from events import views as events_views

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email, password, False)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(events_views.redirect_view)
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect(login_view)
