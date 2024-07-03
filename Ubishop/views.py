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
    

    
@api_view(['DELETE'])
def delete(self, request, id):
    try:
        producto_borrar = productos.objects.get(pk=id) 
        producto_borrar.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
    except productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def insert_product(request):
    try:
        id = request.data.get('id_tienda')
        nombre_producto = request.data.get('nombre_producto')
        descripcion = request.data.get('descripcion', '')
        precio = request.data.get('precio')
        stock = request.data.get('stock')

        if not id or not nombre_producto or not precio or not stock:
            return Response({'error': 'Faltan datos obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

        tienda = Tienda.objects.get(pk=id)

        nuevo_producto = Productos(
            tienda=tienda,
            nombre_producto=nombre_producto,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )

        nuevo_producto.save()
        return Response({'message': 'Producto insertado correctamente'}, status=status.HTTP_201_CREATED)
    except Tienda.DoesNotExist:
        return Response({'error': 'La tienda no existe'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
