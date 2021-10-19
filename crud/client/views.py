from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Clients
from .form import ClientForm
    
def crud(request: HttpRequest) -> HttpResponse:
    '''
    request para acessar a área restrita de usuário com a lista de clientes
    '''
    
    if request.user.is_anonymous or not request.user.is_authenticated:
        return redirect('login')
    
    else:
        data = Clients.objects.filter(owner=request.user.id).order_by('-id')
        
        return render(request=request,
                    template_name="crud.html",
                    context={"clients": data},
                    status=203)   
    

def create(request: HttpRequest) -> HttpResponse:
    
    if request.method == "GET":
    
        form = ClientForm()
        
        return render(request,
                    template_name="create.html",
                    context={"form": form},
                    status=200)
        
    elif request.method == "POST":
        
        print(request.POST)
        
        return redirect('crud')
    
def edit(request: HttpRequest, client_id: id) -> HttpResponse:
    pass

def delete(request: HttpRequest, client_id: id) -> HttpResponse:
    if request.user.is_authenticated:
        client: Clients = Clients.objects.filter(owner=request.user.id).filter(id=client_id).first()
        
        if not client:
            return redirect('crud')
        else:
            client.delete()
            
            return redirect('crud')