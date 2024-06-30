from django.db import models

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'roles'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre_rol

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuarios'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre_usuario

class Perfil(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    ciudad = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'perfil'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre_usuario} {self.apellido_usuario}"

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tiendas'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre

    def obtener_productos(self):
        return Productos.objects.filter(tienda=self)

class Productos(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        db_table = 'productos'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre_producto

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'categoria'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre_categoria

class ProductoCategoria(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = 'producto_categoria'  # Nombre de la tabla en la base de datos
        unique_together = ('producto', 'categoria')

class Inventario(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'inventario'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"Inventario de {self.producto.nombre_producto} en {self.tienda.nombre}"

class Convenio(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    tipo_membresia = models.TextField(null=True, blank=True)
    fecha_convenio_inicio = models.DateField()
    fecha_convenio_fin = models.DateField()

    class Meta:
        db_table = 'Membresia'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"Membresia de {self.tienda.nombre}"

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'reservas'  # Nombre de la tabla en la base de datos

class DetalleReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'detalles_reserva'  # Nombre de la tabla en la base de datos

class Ubicacion(models.Model):
    tienda = models.OneToOneField(Tienda, on_delete=models.CASCADE, primary_key=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    direccion = models.TextField()

    class Meta:
        db_table = 'ubicacion'

    def __str__(self):
        return f"Ubicación de {self.tienda.nombre}"
    
class Resena(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    fecha_opinion = models.DateField()

    class Meta:
        db_table = 'resenas'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"Reseña de {self.usuario.nombre_usuario} - {self.fecha_opinion}"
