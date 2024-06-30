from rest_framework import serializers
from .models import Ubicacion, Productos, Tienda
from django_filters import rest_framework as filter
class UbicacionSerializer(serializers.ModelSerializer):
    tienda = serializers.CharField(source='tienda.nombre')

    class Meta:
        model = Ubicacion
        fields = ['tienda', 'latitud', 'longitud', 'direccion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'nombre_producto', 'descripcion', 'precio', 'stock', 'tienda']

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = ['nombre', 'descripcion']
