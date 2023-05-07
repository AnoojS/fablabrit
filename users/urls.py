from django import urls
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users import views
from .views import user,login,register 

urlpatterns = [
    path("", user, name='user'),
    path("login", login, name='login'),
    path("register", register, name='register'),
    path("UserRegisterapi", views.UserRegister.as_view(), name="UserRegisterapi"),
    path("UserLoginapi", views.UserLogin.as_view(), name="UserLoginapi"),
    path("welcome",views.welcome.as_view(), name='welcome')
]