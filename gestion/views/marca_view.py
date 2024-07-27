from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Marca
from gestion.repositories.marca_repository import MarcaRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class MarcaListView(View):
    def get(self, request, *args, **kwargs):
        repo = MarcaRepository()
        marcas = repo.get_all()
        return render(
            request,
            'marcas/list.html',
            dict(
                marcas=marcas
            )
        )

class MarcaDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = MarcaRepository()
        marca = get_object_or_404(Marca, id=id)
        return render(
            request,
            'marcas/detail.html',
            dict(
                marca=marca
            )
        )

class MarcaDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = MarcaRepository()
        marca = get_object_or_404(Marca, id=id)
        repo.delete(marca)
        return redirect('marca-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class MarcaUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = MarcaRepository()
        marca = get_object_or_404(Marca, id=id)
        return render(
            request,
            'marcas/update.html',
            dict(marca=marca)
        )

    def post(self, request, id, *args, **kwargs):
        repo = MarcaRepository()
        marca = get_object_or_404(Marca, id=id)
        nombre = request.POST.get('nombre')

        repo.update(
            marca=marca,
            nombre=nombre
        )
        return redirect('marca-detail', marca.id)
@method_decorator([login_required, staff_required], name='dispatch')
class MarcaCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'marcas/create.html'
        )

    def post(self, request, *args, **kwargs):
        repo = MarcaRepository()
        nombre = request.POST.get('nombre')

        nueva_marca = repo.create(
            nombre=nombre
        )
        return redirect('marca-detail', nueva_marca.id)
