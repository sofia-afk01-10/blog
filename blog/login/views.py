from django.shortcuts import render, redirect
from .models import User, Role
from .forms import UserForm, RoleForm
from .decorators import login_required, is_director, is_meneger


#страница со списком пользователей
@login_required
def users(request):
    #получим всех пользователей из базы
    users = User.objects.all()
    id = request.session.get('user_id')
    u = User.objects.get(id=id)
    return render(request, 'users.html', {'users': users, 'user':u ,'page': 'users'})

# Create your views here.
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
    else:
        form = UserForm()
    return render(request, "add_user.html", {'form': form, 'page': 'register'})

    
def add_role(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
    else:
        form = RoleForm()
    return render(request, "add_role.html", {'form': form, 'page': 'add_role'})

def index(request):
    if request.session.get('user_id'):
        id = request.session.get('user_id')
        u = User.objects.get(id=id)
        return render (request, 'index.html', {'user': u})
    else:
        return redirect('/login/')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        login = request.POST.get('login')
        password = request.POST.get('pas')

        try:
            user = User.objects.get(login=login)
        except User.DoesNotExist:
            return redirect('/login')

        if password != user.password:
            return redirect('/login')

        request.session['user_id'] = user.id
        request.session['login'] = user.login
        return redirect('/', {'page': 'login'})

def logout_view(request):
    request.session.flush()
    return redirect('/login', {'page': 'logout'})

@login_required
def for_authorized(request):
    return render(request, 'page_for_authorized.html')

@is_director
def for_director(request):
    return render(request, 'page_for_director.html')

@is_meneger
def for_meneger(request):
    return render(request, 'page_for_meneger.html')