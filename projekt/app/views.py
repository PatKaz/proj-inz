from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm  , UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib import messages
from .forms import SignUpForm,EditForm,EmailForm
from django.core.mail import send_mail ,get_connection
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from .decorators import auth_user_should_not_access

@login_required
def home(request):
    return render(request, 'home.html',{})



@auth_user_should_not_access
def start(request):
    return render(request, 'start.html',{})


@auth_user_should_not_access
def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
           # messages.success(request,('Zalogowano poprawnie'))
            return redirect('home')
        else:
            messages.success(request,('Nieprawidłowy login lub hasło -- Spróbuj ponownie'))
            return redirect('login')
    else:
        return render(request, 'login.html',{})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request,('Zostałeś wylogowany'))
    return redirect('login')

@auth_user_should_not_access
def create_user(request):
    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,('Zarejestrowano poprawnie'))
            return redirect('home')
    else:
        form= SignUpForm()
    context= {'form' : form}
    return render(request, 'register.html', context)
@login_required
def profil(request):
    return render(request, 'profil.html', {})

@login_required
def edit(request):
    if request.method == "POST":
        form= EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('Dokonano edycji profilu'))
            return redirect('home')
    else:
        form= EditForm(instance=request.user)
    context= {'form' : form}
    return render(request, 'edit.html',context )

@login_required
def change_password(request):
    if request.method == "POST":
        form= PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,('Dokonano zmiany hasła'))
            return redirect('home')
    else:
        form= PasswordChangeForm(user=request.user)
    context= {'form' : form}
    return render(request, 'change_password.html',context )

def reg(request):
    return render(request, 'reg.html',{})

def pp(request):
    return render(request, 'pp.html',{})
    

@login_required
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        telephone=request.POST.get('telephone')
        content=request.POST.get('content')

        data={
            'name':name,
            'email':email,
            'telephone':telephone,
            'content':content,
        }

        content='''
        Wiadomość od: {}
        Nr tel: {}

        Treść wiadomości: {}
        '''.format(data['email'],data['telephone'],data['content'])
        send_mail(data['name'], content,'', ['emailapp621@gmail.com'])
        messages.success(request,('Wiadomość została wysłana'))
              
    return render(request, 'contact.html', {})