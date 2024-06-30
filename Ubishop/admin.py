from django.contrib import admin
from .models import Rol, Usuario, Perfil, Tienda, Productos, Categoria, ProductoCategoria, Inventario, Convenio, Reserva, DetalleReserva, Ubicacion, Resena
# Register your models here.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(Tienda)
admin.site.register(Productos)
admin.site.register(Categoria)
admin.site.register(ProductoCategoria)
admin.site.register(Inventario)
admin.site.register(Convenio)
admin.site.register(Reserva)
admin.site.register(DetalleReserva)
admin.site.register(Ubicacion)
admin.site.register(Resena)