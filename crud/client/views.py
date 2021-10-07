from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Clients
    
def crud(request: HttpRequest) -> HttpResponse:
    '''
    request para acessar a área restrita de usuário com a lista de clientes
    '''
    
    if request.user.is_anonymous or not request.user.is_authenticated:
        return redirect('login')
    
    data = Clients.objects.filter(published=True)
    
    return render(request=request,
                  template_name="crud.html",
                  context={"clients": data},
                  status=203)   
    

def edit(request: HttpRequest, client_id:int) -> HttpResponse:
    pass

def delete(request: HttpRequest, client: id) -> HttpResponse:
    pass