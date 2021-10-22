from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request: HttpRequest) -> HttpResponse:
    '''
    Request que se relaciona com  área de login do site
    '''
    if request.method == "POST":
        data = request.POST
        print(data)
        if not data["username"].strip() or not data["pass"].strip():
               
            return redirect('login')
        
        login_user = User.objects.filter(username=data["username"])
        if login_user.exists():
            user = auth.authenticate(request,
                              username=data["username"],
                              password=data["pass"])
            if user is not None:
                auth.login(request,
                           user)
                return redirect('crud')
        
        return redirect('login')
    
    elif request.method == "GET":
        if not request.user.is_anonymous:
            redirect('logout')
        return render(request=request,
                    template_name="index.html",
                    context={},
                    status=200)
    
    
def logout(request: HttpRequest):
    '''
    Rota para o logout do usuário
    '''
    if not request.user.is_anonymous:
        auth.logout(request)
        
    return redirect('login')