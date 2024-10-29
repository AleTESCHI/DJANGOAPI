from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # Estas importaciones están correctas
from django.contrib import messages  # Correcto para manejar mensajes flash
from django.contrib.auth.hashers import make_password  # Correcto para encriptar la contraseña
from django.contrib.auth.models import User  # Correcto para usar el modelo User por defecto


# Create your views here.

def login_views(request):
    template_name= "auth-login.html"
         
          #verifica si el usuario ya esta autenticado
    if request.user.is_authenticated and request.user.is_active:
           return redirect('home')
       
   
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:   
                login(request, user)
                return redirect('home')
                
        
                  # Cambia 'home' por la URL o vista a la que quieras redirigir
        else:
            messages.error(request, '¡¡Invalid Login Credential or user is not active!!')
        
    return render(request,template_name) 

# View for register.

def register_views(request):
    template_name= "auth-register.html"
    
    
    if request.method == 'POST':
         username = request.POST['username']
         email = request.POST['email']
         password = request.POST['password']
         password_confirmation = request.POST['password_confirmation']
         
         if password != password_confirmation:
             messages.error(request, 'Las contraseñas no coinciden')
             return render(request, template_name)
         
         if User.objects.filter(username=username).exists():
             messages.error(request, 'El usuario ya existe')
             return render(request, template_name)
         
         if User.objects.filter(email=email).exists():
             messages.error(request, 'El correo ya existe')
             return render(request, template_name)
         
         
         user = User(
             username=username,
             email=email,
             password=make_password(password),
             is_active = 0
         )
         user.save()
         messages.success(request, 'Cuenta creada con exito')
    return render(request,template_name) 

#view for forgot the password
def forgot_views(request):
    template_name= "auth-forgot-password.html"
    
    return render(request,template_name) 

#view for logout
def logout_view(request):
     logout(request)
     return redirect('login')












