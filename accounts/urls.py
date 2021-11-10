from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('restaurants/', views.restaurants, name = 'restaurants'),
    path('search/', views.search, name = 'search'),
    path('profile/', views.profile, name = 'profile'),
    path('userLogin/', views.userLogin, name = 'userLogin'),
    path('logoutUser/', views.logoutUser, name = 'logoutUser'),
    path('userRegister/', views.userRegister, name = 'userRegister'),
]