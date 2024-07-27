# gestion/views/cliente_view.py
from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Cliente
from gestion.forms import ClienteForm
from gestion.repositories.cliente_repository import ClienteRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ClienteListView(View):
    def get(self, request, *args, **kwargs):
        repo = ClienteRepository()
        clientes = repo.get_all()
        return render(
            request,
            'clientes/list.html',
            dict(
                clientes=clientes
            )
        )

class ClienteDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ClienteRepository()
        cliente = get_object_or_404(Cliente, id=id)
        return render(
            request,
            'clientes/detail.html',
            dict(
                cliente=cliente
            )
        )

class ClienteDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = ClienteRepository()
        cliente = get_object_or_404(Cliente, id=id)
        repo.delete(cliente)
        return redirect('cliente-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class ClienteUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ClienteRepository()
        cliente = get_object_or_404(Cliente, id=id)
        form = ClienteForm(instance=cliente)
        return render(
            request,
            'clientes/update.html',
            {'form': form}
        )

    def post(self, request, id, *args, **kwargs):
        repo = ClienteRepository()
        cliente = get_object_or_404(Cliente, id=id)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente-detail', cliente.id)
        return render(request, 'clientes/update.html', {'form': form})

@method_decorator([login_required, staff_required], name='dispatch')
class ClienteCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        return render(
            request,
            'clientes/create.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente-detail', form.instance.id)
        return render(request, 'clientes/create.html', {'form': form})

