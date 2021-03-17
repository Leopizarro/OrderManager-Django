"""techkchallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import product_create_view, product_individual_view, products_list_view
from users.views import user_register_view
from django.contrib.auth import views as auth_views
from motoristas.views import create_motorista_view, motorista_list_view
from pedidos.views import pedido_create_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_list_view, name='home-products'),
    path('products/', products_list_view, name='products'),
    path('create/', product_create_view),
    path('products/<int:id>/', product_individual_view),
    path('register/', user_register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/user_login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/user_logout.html'), name="logout"),
    path('motoristas/create/', create_motorista_view, name='crear_motorista'),
    path('motoristas/', motorista_list_view, name='motoristas'),
    path('order/<int:uid>/<int:pid>/', pedido_create_view, name= 'create_order' )
]
