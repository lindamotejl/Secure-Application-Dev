from django.urls import path
from django.contrib.auth import views as auth_views
from users.forms import UserLoginForm
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]