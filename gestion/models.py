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
    """
    Modelo que representa un modelo específico de auto, asociado a una marca.
    """
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que es el nombre del modelo.
        """
        return f'{self.nombre}'

class Categoria(models.Model):
    """
    Modelo que representa una categoría de autos.
    """
    nombre = models.CharField(max_length=100)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que es el nombre de la categoría.
        """
        return self.nombre

class Auto(models.Model):
    """
    Modelo que representa un auto específico con detalles como marca, modelo, categoría, precio, imagen y descripción.
    """
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default=1)
    modelo = models.ForeignKey(ModeloAuto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='autos/')
    descripcion = models.TextField()

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que es la marca y el modelo del auto.
        """
        return f'{self.modelo.marca} {self.modelo.nombre}'

class Cliente(models.Model):
    """
    Modelo que representa un cliente, que está relacionado uno a uno con un usuario del sistema.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que es el nombre de usuario del cliente.
        """
        return self.user.username

class Comentario(models.Model):
    """
    Modelo que representa un comentario hecho por un usuario sobre un auto.
    """
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que incluye el nombre de usuario del autor y el nombre del modelo del auto.
        """
        return f'{self.autor.username} - {self.auto.modelo.nombre}'

class Venta(models.Model):
    """
    Modelo que representa una venta de un auto a un cliente, con detalles de fecha y precio final.
    """
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que incluye el nombre de usuario del cliente y el nombre del modelo del auto vendido.
        """
        return f'{self.cliente.user.username} - {self.auto.modelo.nombre}'

class Empleado(models.Model):
    """
    Modelo que representa un empleado de la concesionaria, vinculado a un usuario del sistema.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=100)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que es el nombre de usuario del empleado.
        """
        return self.user.username

class Proveedor(models.Model):
    """
    Modelo que representa un proveedor que suministra autos a la concesionaria.
    """
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    autos = models.ManyToManyField(Auto)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que es el nombre del proveedor.
        """
        return self.nombre

class Servicio(models.Model):
    """
    Modelo que representa un servicio ofrecido por la concesionaria.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que es el nombre del servicio.
        """
        return self.nombre

class Cita(models.Model):
    """
    Modelo que representa una cita de un cliente para un servicio específico.
    """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    descripcion = models.TextField()

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que incluye el nombre de usuario del cliente y el nombre del servicio.
        """
        return f'{self.cliente.user.username} - {self.servicio.nombre}'

class Inventario(models.Model):
    """
    Modelo que representa el inventario de autos en la concesionaria, con la cantidad disponible y fecha de actualización.
    """
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que incluye el nombre del modelo del auto y la cantidad disponible.
        """
        return f'Inventario {self.auto.modelo.nombre} - {self.cantidad}'

class Financiamiento(models.Model):
    """
    Modelo que representa un financiamiento otorgado a un cliente para la compra de un auto.
    """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    monto_financiado = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2)
    plazo_meses = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que incluye el nombre de usuario del cliente y el nombre del modelo del auto.
        """
        return f'Financiamiento {self.cliente.user.username} - {self.auto.modelo.nombre}'
