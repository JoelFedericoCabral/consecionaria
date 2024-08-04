from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthView(View):
    """
    Vista para manejar el registro e inicio de sesión de usuarios.

    Esta vista gestiona tanto el registro como el inicio de sesión de usuarios, utilizando
    un único formulario que cambia su comportamiento según los datos recibidos.
    """
    def get(self, request):
        """
        Maneja las peticiones GET para mostrar los formularios de login y registro.

        Renderiza la plantilla de autenticación con los formularios de inicio de sesión y registro.
        """
        login_form = UserLoginForm()
        register_form = UserRegistrationForm()
        return render(request, 'home/auth.html', {'login_form': login_form, 'register_form': register_form})

    def post(self, request):
        """
        Maneja las peticiones POST para procesar el registro o inicio de sesión.

        - Procesa el registro de un nuevo usuario si se reciben los campos de registro.
        - Procesa el inicio de sesión de un usuario existente si se reciben los campos de inicio de sesión.
        """
        # Procesar registro de usuario
        if 'username' in request.POST and 'password1' in request.POST and 'password2' in request.POST:
            register_form = UserRegistrationForm(request.POST)
            if register_form.is_valid():
                new_user = register_form.save(commit=False)
                new_user.set_password(register_form.cleaned_data['password1'])
                new_user.save()
                user = authenticate(username=new_user.username, password=register_form.cleaned_data['password1'])
                if user:
                    login(request, user)
                    return redirect('index')
            else:
                return render(request, 'home/auth.html', {'register_form': register_form, 'login_form': UserLoginForm()})
        # Procesar inicio de sesión de usuario
        elif 'username' in request.POST and 'password' in request.POST:
            login_form = UserLoginForm(data=request.POST)
            if login_form.is_valid():
                user = authenticate(request, username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
                if user:
                    login(request, user)
                    return redirect('index')
            return render(request, 'home/auth.html', {'login_form': login_form, 'register_form': UserRegistrationForm()})
        return redirect('login')

class LogoutView(View):
    """
    Vista para manejar el cierre de sesión de los usuarios.

    Esta vista simplemente cierra la sesión del usuario actual y redirige a la página de inicio de sesión.
    """
    def get(self, request):
        """
        Maneja las peticiones GET para cerrar la sesión del usuario.

        Redirige al usuario a la página de inicio de sesión después de cerrar sesión.
        """
        logout(request)
        return redirect('login')


class RegisterView(View):
    """
    Vista para manejar el registro de nuevos usuarios.

    Proporciona un formulario para que los nuevos usuarios se registren en el sistema.
    """
    def get(self, request):
        """
        Maneja las peticiones GET para mostrar el formulario de registro.

        Renderiza la plantilla de registro con el formulario correspondiente.
        """
        form = UserRegistrationForm()
        return render(request, 'home/register.html', {'form': form})

    def post(self, request):
        """
        Maneja las peticiones POST para procesar el formulario de registro.

        Crea un nuevo usuario si el formulario es válido y lo autentica automáticamente.
        """
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            user = authenticate(username=new_user.username, password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'home/register.html', {'form': form})

class IndexView(LoginRequiredMixin, TemplateView):
    """
    Vista para la página de inicio principal del sistema.

    Esta vista utiliza un TemplateView genérico y requiere que el usuario esté autenticado para acceder.
    """
    template_name = 'home/index.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        """
        Proporciona el contexto adicional para la plantilla de inicio.

        Añade el usuario autenticado al contexto de la plantilla.
        """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
