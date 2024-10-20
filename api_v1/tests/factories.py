import factory
from gestion.models import Auto, Categoria, Marca, ModeloAuto

class MarcaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Marca

    nombre = factory.Faker('company')

class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria

    nombre = factory.Faker('word')

class ModeloAutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloAuto

    marca = factory.SubFactory(MarcaFactory)
    nombre = factory.Faker('word')

class AutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Auto

    categoria = factory.SubFactory(CategoriaFactory)
    modelo = factory.SubFactory(ModeloAutoFactory)
    marca = factory.SubFactory(MarcaFactory)
    precio = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    imagen = None
    # imagen = factory.django.ImageField(filename='auto.jpg')
    descripcion = factory.Faker('text')
