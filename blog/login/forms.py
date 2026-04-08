from .models import User, Role
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'first_name', 'last_name', 'age']
        labels = {
            'login': 'Логин',
            'password': 'Пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'age': 'Возраст',
            'role': 'Роль',
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']
        labels = {
            'name': 'Название',
        }