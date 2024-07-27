from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Inventario, Auto
from gestion.repositories.inventario_repository import InventarioRepository
from gestion.forms import InventarioForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class InventarioListView(View):
    def get(self, request, *args, **kwargs):
        repo = InventarioRepository()
        inventarios = repo.get_all()
        return render(
            request,
            'inventarios/list.html',
            dict(
                inventarios=inventarios
            )
        )

class InventarioDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = InventarioRepository()
        inventario = get_object_or_404(Inventario, id=id)
        return render(
            request,
            'inventarios/detail.html',
            dict(
                inventario=inventario
            )
        )

class InventarioDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = InventarioRepository()
        inventario = get_object_or_404(Inventario, id=id)
        repo.delete(inventario)
        return redirect('inventario-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class InventarioUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = InventarioRepository()
        inventario = get_object_or_404(Inventario, id=id)
        form = InventarioForm(instance=inventario)
        return render(
            request,
            'inventarios/update.html',
            dict(
                form=form
            )
        )

    def post(self, request, id, *args, **kwargs):
        repo = InventarioRepository()
        inventario = get_object_or_404(Inventario, id=id)
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('inventario-detail', inventario.id)
        return render(request, 'inventarios/update.html', {'form': form})

@method_decorator([login_required, staff_required], name='dispatch')
class InventarioCreateView(View):
    def get(self, request, *args, **kwargs):
        form = InventarioForm()
        return render(request, 'inventarios/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = InventarioForm(request.POST)
        if form.is_valid():
            nuevo_inventario = form.save()
            return redirect('inventario-detail', nuevo_inventario.id)
        return render(request, 'inventarios/create.html', {'form': form})
