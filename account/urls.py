from django.contrib import admin
from django.urls import path, include
from account.views import login_account, register_account, editar_usuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('editar/usuario', editar_usuario, name="accountEditarUsuario"),
    path('login/', login_account, name="accountlogin"),
    path('registrar/', register_account, name="accountRegistrar"),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="accountlogout")
]