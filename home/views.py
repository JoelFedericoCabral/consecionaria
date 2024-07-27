from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthView(View):
    def get(self, request):
        login_form = UserLoginForm()
        register_form = UserRegistrationForm()
        return render(request, 'home/auth.html', {'login_form': login_form, 'register_form': register_form})

    def post(self, request):
        if 'username' in request.POST and 'password' in request.POST:
            login_form = UserLoginForm(data=request.POST)
            if login_form.is_valid():
                user = authenticate(request, username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
                if user:
                    login(request, user)
                    return redirect('index')
            return render(request, 'home/auth.html', {'login_form': login_form, 'register_form': UserRegistrationForm()})
        elif 'username' in request.POST and 'password1' in request.POST and 'password2' in request.POST:
            register_form = UserRegistrationForm(request.POST)
            if register_form.is_valid():
                new_user = register_form.save(commit=False)
                new_user.set_password(register_form.cleaned_data['password1'])
                new_user.save()
                user = authenticate(username=new_user.username, password=register_form.cleaned_data['password1'])
                if user is not None:
                    login(request, user)
                    return redirect('index')
            return render(request, 'home/auth.html', {'register_form': register_form, 'login_form': UserLoginForm()})
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'home/register.html', {'form': form})

    def post(self, request):
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
    template_name = 'home/index.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
