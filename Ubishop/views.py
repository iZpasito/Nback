from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Ubicacion, Productos, Tienda
from .serializers import ProductoSerializer, TiendaSerializer, UbicacionSerializer

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
