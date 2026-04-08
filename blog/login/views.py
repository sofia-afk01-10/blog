from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm, RoleForm

def main(request):
    return render(request, 'base.html', {'page': 'main'})

#страница со списком пользователей
def users(request):
    #получим всех пользователей из базы
    users = User.objects.all()
    return render(request, 'users.html', {'users': users, 'page': 'users'})

# Create your views here.
def add_user(request):
    # получили данные. нужно сохранить юзера в базу
    if request.method == "POST":
        # получаем данные из формы
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('/users/')
    # это простой запрос, нужно показать форму
    else:
        form = UserForm()
        return render(request, "add_user.html", {'form': form})
    
def add_role(request):
    if request.method == "POST":
        role = RoleForm(request.POST)
        if role.is_valid():
            role.save()
            return redirect('/users/')
    else:
        form = RoleForm()
        return render(request, "add_role.html", {'form': form})