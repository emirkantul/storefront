from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views #import this
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name = 'home'),
    path('restaurants/', views.restaurants, name = 'restaurants'),
    path('search/', views.search, name = 'search'),
    path('profile/', views.profile, name = 'profile'),
    path('userLogin/', views.userLogin, name = 'userLogin'),
    path('logoutUser/', views.logoutUser, name = 'logoutUser'),
    path('userRegister/', views.userRegister, name = 'userRegister'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)