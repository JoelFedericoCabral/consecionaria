from django.db import models
from django.contrib.auth.models import User



class Marca(models.Model):
    """
    Modelo que representa una marca de autos.
    """
    nombre = models.CharField(max_length=100)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que es el nombre de la marca.
        """
        return self.nombre


class ModeloAuto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default=1)
    modelo = models.ForeignKey(ModeloAuto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.modelo.marca} {self.modelo.nombre}'


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Comentario(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.username} - {self.auto.modelo.nombre}'


class Venta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cliente.user.username} - {self.auto.modelo.nombre}'


class Empleado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, default="Nombre")
    apellido = models.CharField(max_length=100, default="Apellido")
    telefono = models.CharField(max_length=15, default="+Telefono")
    dni = models.CharField(max_length=10, unique=True, default="DNI")
    direccion = models.CharField(max_length=255, default="Direccion")
    puesto = models.CharField(max_length=100, default="Puesto")

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.user.username})'


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    autos = models.ManyToManyField(Auto)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.cliente.user.username} - {self.servicio.nombre}'


class Inventario(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Inventario {self.auto.modelo.nombre} - {self.cantidad}'


class Financiamiento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    monto_financiado = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2)
    plazo_meses = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f'Financiamiento {self.cliente.user.username} - {self.auto.modelo.nombre}'
