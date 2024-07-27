from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Proveedor
from gestion.repositories.proveedor_repository import ProveedorRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProveedorListView(View):
    def get(self, request, *args, **kwargs):
        repo = ProveedorRepository()
        proveedores = repo.get_all()
        return render(
            request,
            'proveedores/list.html',
            dict(
                proveedores=proveedores
            )
        )

class ProveedorDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ProveedorRepository()
        proveedor = get_object_or_404(Proveedor, id=id)
        return render(
            request,
            'proveedores/detail.html',
            dict(
                proveedor=proveedor
            )
        )

class ProveedorDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = ProveedorRepository()
        proveedor = get_object_or_404(Proveedor, id=id)
        repo.delete(proveedor)
        return redirect('proveedor-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class ProveedorUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ProveedorRepository()
        proveedor = get_object_or_404(Proveedor, id=id)
        return render(
            request,
            'proveedores/update.html',
            dict(proveedor=proveedor)
        )

    def post(self, request, id, *args, **kwargs):
        repo = ProveedorRepository()
        proveedor = get_object_or_404(Proveedor, id=id)
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        repo.update(
            proveedor=proveedor,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono
        )
        return redirect('proveedor-detail', proveedor.id)

@method_decorator([login_required, staff_required], name='dispatch')
class ProveedorCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'proveedores/create.html'
        )

    def post(self, request, *args, **kwargs):
        repo = ProveedorRepository()
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        nuevo_proveedor = repo.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono
        )
        return redirect('proveedor-detail', nuevo_proveedor.id)
