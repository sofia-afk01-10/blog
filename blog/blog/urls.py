#from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.main),
    path('', views.index),
    path('add_user/', views.add_user),
    path('users/', views.users),
    path('add_role/', views.add_role),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('page1/', views.for_authorized),
    path('page2/', views.for_director),
    path('page3/', views.for_meneger),
]
