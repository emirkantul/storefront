from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('signin',views.signin, name='signin'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('rez',views.rez,name='rez'),

]