from django import forms
from gestion.models import Auto, Marca, ModeloAuto, Categoria, Inventario, Cliente, Comentario, Empleado
from django.contrib.auth.models import User

class AutoForm(forms.ModelForm):
    """
    Formulario para crear y editar objetos de tipo Auto.

    Este formulario se basa en el modelo Auto e incluye campos
    para la marca, el modelo, la categoría, el precio, la imagen
    y la descripción del auto.
    """
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
        label='Marca',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    modelo = forms.ModelChoiceField(
        queryset=ModeloAuto.objects.all(),
        label='Modelo',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        label='Categoría',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    precio = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    imagen = forms.ImageField()

    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'categoria', 'precio', 'imagen', 'descripcion']

    def __init__(self, *args, **kwargs):
        """
        Inicializa el formulario de Auto, ajustando el queryset del campo 'modelo'
        basado en la selección de 'marca' para permitir la selección dinámica de modelos
        según la marca seleccionada.
        """
        super().__init__(*args, **kwargs)
        if 'marca' in self.data:
            try:
                marca_id = int(self.data.get('marca'))
                self.fields['modelo'].queryset = ModeloAuto.objects.filter(marca_id=marca_id).order_by('nombre')
            except (ValueError, TypeError):
                self.fields['modelo'].queryset = ModeloAuto.objects.all()
        elif self.instance.pk:
            self.fields['modelo'].queryset = self.instance.marca.modeloauto_set.order_by('nombre')
        else:
            self.fields['modelo'].queryset = ModeloAuto.objects.all()

class InventarioForm(forms.ModelForm):
    """
    Formulario para gestionar el inventario de autos.

    Incluye campos para seleccionar el auto y especificar
    la cantidad disponible.
    """
    class Meta:
        model = Inventario
        fields = ['auto', 'cantidad']
        widgets = {
            'auto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    """
    Formulario para gestionar los datos de un cliente.

    Incluye campos para seleccionar el usuario asociado y
    capturar el teléfono y la dirección del cliente.
    """
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Usuario',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        max_length=15,
        label='Teléfono',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        max_length=255,
        label='Dirección',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Cliente
        fields = ['user', 'telefono', 'direccion']

class ComentarioForm(forms.ModelForm):
    """
    Formulario para añadir comentarios a los autos.

    Incluye campos para seleccionar el auto y escribir el comentario.
    """
    class Meta:
        model = Comentario
        fields = ['auto', 'comentario']
        widgets = {
            'auto': forms.Select(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'telefono', 'dni', 'direccion', 'puesto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control'}),
        }


