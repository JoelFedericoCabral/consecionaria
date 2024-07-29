from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import ModeloAuto, Marca
from gestion.repositories.modelo_auto_repository import ModeloAutoRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ModeloAutoListView(View):
    def get(self, request, *args, **kwargs):
        repo = ModeloAutoRepository()
        modelos = repo.get_all()
        return render(
            request,
            'modelos/list.html',
            dict(
                modelos=modelos
            )
        )

class ModeloAutoDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ModeloAutoRepository()
        modelo = get_object_or_404(ModeloAuto, id=id)
        return render(
            request,
            'modelos/detail.html',
            dict(
                modelo=modelo
            )
        )

class ModeloAutoDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = ModeloAutoRepository()
        modelo = get_object_or_404(ModeloAuto, id=id)
        repo.delete(modelo)
        return redirect('modelo-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class ModeloAutoUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ModeloAutoRepository()
        modelo = get_object_or_404(ModeloAuto, id=id)
        marcas = Marca.objects.all()
        return render(
            request,
            'modelos/update.html',
            dict(
                modelo=modelo,
                marcas=marcas
            )
        )

    def post(self, request, id, *args, **kwargs):
        repo = ModeloAutoRepository()
        modelo = get_object_or_404(ModeloAuto, id=id)
        marca = get_object_or_404(Marca, id=request.POST.get('marca_id'))
        nombre = request.POST.get('nombre')

        repo.update(
            modelo=modelo,
            marca=marca,
            nombre=nombre
        )
        return redirect('modelo-detail', modelo.id)
@method_decorator([login_required, staff_required], name='dispatch')
class ModeloAutoCreateView(View):
    def get(self, request, *args, **kwargs):
        marcas = Marca.objects.all()
        return render(
            request,
            'modelos/create.html',
            dict(
                marcas=marcas
            )
        )

    def post(self, request, *args, **kwargs):
        repo = ModeloAutoRepository()
        marca = get_object_or_404(Marca, id=request.POST.get('marca_id'))
        nombre = request.POST.get('nombre')

        nuevo_modelo = repo.create(
            marca=marca,
            nombre=nombre
        )
        return redirect('modelo-detail', nuevo_modelo.id)