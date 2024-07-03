from rest_framework import serializers
from .models import Ubicacion, Productos, Tienda, Usuario
from django_filters import rest_framework as filter
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'email', 'rol']

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

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