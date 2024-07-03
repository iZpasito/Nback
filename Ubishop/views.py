from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Ubicacion, Productos, Tienda, Usuario, Rol
from .serializers import ProductoSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth.models import User


@api_view(['POST'])

def login(request):
    try:
        user = Usuario.objects.get(email=request.data['email'])
    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(request.data['password']):
        return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def buscar_productos(request):
    query = request.GET.get('q', '')
    if query:
        productos = Productos.objects.filter(nombre_producto__icontains=query)
    else:
        productos = Productos.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    data = [
        {
            'tienda': ubicacion.tienda.nombre,
            'descripcion': ubicacion.tienda.descripcion,
            'latitud': float(ubicacion.latitud),
            'longitud': float(ubicacion.longitud),
            'direccion': ubicacion.direccion,
            'tienda_id': ubicacion.tienda.id
        }
        for ubicacion in ubicaciones
    ]
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def productos_por_tienda(request, tienda_id):
    productos = Productos.objects.filter(tienda_id=tienda_id)
    data = [
        {
            'nombre_producto': producto.nombre_producto,
            'descripcion': producto.descripcion,
            'precio': float(producto.precio),
            'stock': producto.stock
        }
        for producto in productos
    ]
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def productos(request):
    productos_all = Productos.objects.all()
    data = [
        {
            'nombre_producto': producto.nombre_producto,
            'descripcion': producto.descripcion,
            'precio': float(producto.precio),
            'stock': producto.stock
        }
        for producto in productos_all
    ]
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def tiendas(request):
    tiendas = Tienda.objects.all()
    data = [
        {
            'nombre': tienda.nombre,
            'descripcion': tienda.descripcion,
            'propietario': tienda.propietario.nombre_usuario,
            'propietario_id': tienda.propietario.id
        }
        for tienda in tiendas
    ]
    return JsonResponse(data, safe=False)