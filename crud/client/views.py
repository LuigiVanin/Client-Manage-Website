from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from .models import Clients
from .form import ClientForm
    
    
def crud(request: HttpRequest) -> HttpResponse:
    '''Requisição para acessar a área restrita de usuário com a lista de clientes'''

    if request.user.is_anonymous or not request.user.is_authenticated:
        return redirect('login')
    else:
        data = Clients.objects.filter(owner=request.user.id).order_by('-id')
        
        return render(request=request,
                    template_name="crud.html",
                    context={"clients": data},
                    status=203)   
    

def create(request: HttpRequest) -> HttpResponse:
    '''Cria um cliente para o usuário logado'''
    
    if request.method == "GET":
        form = ClientForm(initial={"debt": None})    
        return render(request,
                    template_name="create.html",
                    context={"form": form},
                    status=200)
        
    elif request.method == "POST":
        if not ("create" in request.path):
            return redirect('crud')
        data = request.POST
        owner = User.objects.filter(id=request.user.id).first()
        if owner == None:
            return redirect('login')
        Clients.objects.create(name=data["name"].upper(),
                               surname=data["surname"].upper(),
                               email=data["email"],
                               age=data["age"],
                               debt=data["debt"],
                               owner=owner)
        return redirect('crud')
  
    
def edit(request: HttpRequest, client_id: id) -> HttpResponse:
    '''Requisição que edita um cliente do usuário logado'''
    
    if not request.user.is_authenticated:
        return redirect('login')
    client: Clients = Clients.objects.filter(owner=request.user.id).filter(id=client_id).first()
    if not client:
        return redirect('crud')
    if request.method == "GET":
        form = ClientForm(initial={"name": client.name,
                                   "surname": client.surname,
                                   "email": client.email,
                                   "age": client.age,
                                   "debt": client.debt})
        return render(request,
                      template_name='edit.html',
                      context={"form": form, "client": client},
                      status=200)
    if request.method == "POST":
        data = request.POST
        if not ("edit/{}".format(client_id) in request.path):
            return redirect('login') 
        
        client.name = data["name"].upper()
        client.surname = data["surname"].upper()
        client.email = data["email"]
        client.age = data["age"]
        client.debt = data["debt"]
        client.save()
        
        return redirect('crud')
 

def delete(request: HttpRequest, client_id: id) -> HttpResponse:
    '''Requisição que apaga um dos clientes do usuário logado'''
    
    if request.user.is_authenticated:
        client: Clients = Clients.objects.filter(owner=request.user.id).filter(id=client_id).first()
        if not client:    
            return redirect('crud')
        else:
            client.delete()
            
            return redirect('crud')