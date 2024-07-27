from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellidos', max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password1') != cd.get('password2'):
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd.get('password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', max_length=30)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


