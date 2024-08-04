from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    """
    Formulario para el registro de nuevos usuarios.

    Proporciona campos para capturar información básica del usuario,
    incluyendo nombre de usuario, nombre, apellidos, correo electrónico
    y contraseña. Implementa una validación para asegurar que las contraseñas coincidan.
    """
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellidos', max_length=30)
    email = forms.EmailField(label='Correo Electrónico')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        error_messages = {
            'username': {
                'max_length': "Nombre de usuario demasiado largo. Máximo 150 caracteres.",
                'required': "Este campo es obligatorio.",
                'invalid': "El nombre de usuario solo puede contener letras, números y @/./+/-/_",
            },
            'email': {
                'invalid': "Por favor, introduce una dirección de correo electrónico válida.",
            },
        }

    def __init__(self, *args, **kwargs):
        """
        Inicializa el formulario de registro de usuario.

        Elimina el texto de ayuda y los sufijos de etiqueta de los campos.
        """
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None
            field.label_suffix = ''

    def clean_password2(self):
        """
        Verifica que las contraseñas ingresadas coincidan.

        Lanza una ValidationError si las contraseñas no son iguales.
        """
        cd = self.cleaned_data
        if cd.get('password1') != cd.get('password2'):
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd.get('password2')

class UserLoginForm(AuthenticationForm):
    """
    Formulario de autenticación para el inicio de sesión de usuarios.

    Permite a los usuarios autenticarse proporcionando un nombre de usuario y una contraseña.
    """
    username = forms.CharField(label='Usuario', max_length=30)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
