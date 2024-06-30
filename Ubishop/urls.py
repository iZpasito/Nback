from django.urls import path
from . import views

urlpatterns = [
    path('ubicaciones/', views.ubicaciones, name='ubicaciones'),
    path('tiendas/', views.tiendas, name='tiendas'),
    path('tiendas/<int:tienda_id>/productos/', views.productos_por_tienda, name='productos_por_tienda'),
    path('productos/', views.productos, name='productos'),
    path('buscar/', views.buscar_productos, name='buscar_productos')
]