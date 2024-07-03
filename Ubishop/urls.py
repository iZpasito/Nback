from django.urls import path
from rest_framework.authtoken import views
from .views import login, register, insert_product, delete, buscar_productos, ubicaciones, productos_por_tienda, productos, tiendas

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('insert_product/', insert_product, name='insert_product'),
    path('delete/<int:id>/', delete, name='delete'),
    path('buscar_productos/', buscar_productos, name='buscar_productos'),
    path('ubicaciones/', ubicaciones, name='ubicaciones'),
    path('productos_por_tienda/<int:tienda_id>/', productos_por_tienda, name='productos_por_tienda'),
    path('productos/', productos, name='productos'),
    path('tiendas/', tiendas, name='tiendas'),
]