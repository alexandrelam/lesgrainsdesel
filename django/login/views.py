from django.shortcuts import render
from django.contrib.auth import login, logout
from odooAuth import models as auth
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from events import views as events_views


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        odooBackend = auth.OdooBackend()
        user = odooBackend.authenticate(request, email, password, False)
        if user is not None:
            print("[DEBUG] User id is "+ str(user.getUserId()))
            print("[DEBUG] Logging in...")
            login(request, user)
            return redirect(events_views.redirect_view)
    return render(request, 'login/login.html')


def logout_view(request):
    current_user = request.user
    print("[DEBUG] Logging out and deleting user : "+str(current_user.getFullName())+
            " ID : "+str(current_user.getUserId()))
    logout(request)
    current_user.delete()
    return redirect(login_view)
