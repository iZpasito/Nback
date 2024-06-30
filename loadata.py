# load_data.py

import os
import django
from datetime import date
from django.utils.timezone import make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ubis.settings')
django.setup()

from Ubishop.models import Rol, Usuario, Perfil, Tienda, Categoria, Productos, Inventario, Convenio, Reserva, DetalleReserva, Ubicacion, Resena

# Insertar roles
roles_data = [
    ('Administrador', 'Rol con privilegios de administrador del sistema'),
    ('Vendedor', 'Rol para usuarios encargados de la venta de productos'),
    ('Cliente', 'Rol para usuarios que compran productos en la tienda'),
]

for nombre_rol, descripcion in roles_data:
    Rol.objects.create(nombre_rol=nombre_rol, descripcion=descripcion)

# Insertar usuarios
usuarios_data = [
    ('admin', 'root', 'admin@gmail.com', 1),
    ('Vendedor', 'vende', 'vendedor@gmail.com', 2),
    ('cliente', 'client', 'cliente@gmail.com', 3),
]

for nombre_usuario, clave, email, rol_id in usuarios_data:
    rol = Rol.objects.get(pk=rol_id)
    Usuario.objects.create(nombre_usuario=nombre_usuario, clave=clave, email=email, rol=rol)

# Insertar perfiles
perfiles_data = [
    (1, 'admin', 'Admin', '123456789', 'talca', '123 Main St', 'admin@gmail.com'),
    (2, 'Vendedor', 'Uno', '987654321', 'talca', '456 Elm St', 'vendedor@gmail.com'),
    (3, 'cliente', 'Uno', '555555555', 'talca', '789 Oak St', 'cliente@gmail.com'),
]

for usuario_id, nombre_usuario, apellido_usuario, telefono, ciudad, direccion, email in perfiles_data:
    usuario = Usuario.objects.get(pk=usuario_id)
    Perfil.objects.create(usuario=usuario, nombre_usuario=nombre_usuario, apellido_usuario=apellido_usuario, telefono=telefono, ciudad=ciudad, direccion=direccion, email=email)

# Insertar tiendas
tiendas_data = [
    ('Jumbo', 'Supermercado del Elefante', 2),
    ('Unimarc', 'Supermercado de la U', 3),
]

for nombre, descripcion, propietario_id in tiendas_data:
    propietario = Usuario.objects.get(pk=propietario_id)
    Tienda.objects.create(nombre=nombre, descripcion=descripcion, propietario=propietario)

# Insertar categorías
categorias_data = [
    ('Supermercado', 'Todo tipo de productos'),
    ('Ropa', 'Ropa y accesorios de moda'),
    ('Hogar', 'Artículos para el hogar y decoración'),
]

for nombre_categoria, descripcion in categorias_data:
    Categoria.objects.create(nombre_categoria=nombre_categoria, descripcion=descripcion)

# Insertar productos
productos_data = [
    (1, 'Red Bull', 'Energetica', 1890, 10),
    (1, 'Zofrito', 'Zofrito para la comida', 900, 20),
    (2, 'Bebida 2 litros Coca Cola', 'Bebida', 1490, 5),
]

for tienda_id, nombre_producto, descripcion, precio, stock in productos_data:
    tienda = Tienda.objects.get(pk=tienda_id)
    Productos.objects.create(tienda=tienda, nombre_producto=nombre_producto, descripcion=descripcion, precio=precio, stock=stock)

# Insertar inventario
inventarios_data = [
    (1, 1, 5),
    (1, 2, 10),
    (2, 3, 2),
]

for tienda_id, producto_id, cantidad in inventarios_data:
    tienda = Tienda.objects.get(pk=tienda_id)
    producto = Productos.objects.get(pk=producto_id)
    Inventario.objects.create(tienda=tienda, producto=producto, cantidad=cantidad)

# Insertar convenios
convenios_data = [
    (1, '2024-06-01', '2029-12-31'),
    (2, '2024-06-01', '2028-11-15'),
]

for tienda_id, fecha_convenio_inicio, fecha_convenio_fin in convenios_data:
    tienda = Tienda.objects.get(pk=tienda_id)
    Convenio.objects.create(tienda=tienda, fecha_convenio_inicio=fecha_convenio_inicio, fecha_convenio_fin=fecha_convenio_fin)

# Insertar reservas
reservas_data = [
    (3, '2024-06-03', 1500),
    (3, '2024-06-03', 1700),
]

for usuario_id, fecha, total in reservas_data:
    usuario = Usuario.objects.get(pk=usuario_id)
    Reserva.objects.create(usuario=usuario, fecha=fecha, total=total)

# Insertar detalles de reserva
detalles_reserva_data = [
    (1, 1, 1, 1500),
    (2, 2, 2, 1700),
]

for reserva_id, producto_id, cantidad, precio in detalles_reserva_data:
    reserva = Reserva.objects.get(pk=reserva_id)
    producto = Productos.objects.get(pk=producto_id)
    DetalleReserva.objects.create(reserva=reserva, producto=producto, cantidad=cantidad, precio=precio)

# Insertar ubicaciones
ubicaciones_data = [
    (1, -35.4295325473251, -71.61831152527762, 'Las rastras. Av. 2 Norte, 3230, Talca, Chile'),
    (2, -35.43214797504574, -71.62753235025843, '5 Norte 3615, Talca, Chile'),
]

for tienda_id, latitud, longitud, direccion in ubicaciones_data:
    tienda = Tienda.objects.get(pk=tienda_id)
    Ubicacion.objects.create(tienda=tienda, latitud=latitud, longitud=longitud, direccion=direccion)

# Insertar reseñas
resenas_data = [
    (3, 5, '¡Excelente servicio!', '2024-06-03'),
    (3, 5, 'Muy buenos productos', '2024-06-03'),
]

for usuario_id, calificacion, comentario, fecha_opinion in resenas_data:
    usuario = Usuario.objects.get(pk=usuario_id)
    Resena.objects.create(usuario=usuario, calificacion=calificacion, comentario=comentario, fecha_opinion=fecha_opinion)
