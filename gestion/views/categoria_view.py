from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Categoria
from gestion.repositories.categoria_repository import CategoriaRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CategoriaListView(View):
    def get(self, request, *args, **kwargs):
        repo = CategoriaRepository()
        categorias = repo.get_all()
        return render(
            request,
            'categorias/list.html',
            dict(
                categorias=categorias
            )
        )

class CategoriaDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = CategoriaRepository()
        categoria = get_object_or_404(Categoria, id=id)
        return render(
            request,
            'categorias/detail.html',
            dict(
                categoria=categoria
            )
        )

class CategoriaDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = CategoriaRepository()
        categoria = get_object_or_404(Categoria, id=id)
        repo.delete(categoria)
        return redirect('categoria-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])





@method_decorator(login_required, name='dispatch')
class CategoriaUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = CategoriaRepository()
        categoria = get_object_or_404(Categoria, id=id)
        return render(
            request,
            'categorias/update.html',
            dict(categoria=categoria)
        )

    def post(self, request, id, *args, **kwargs):
        repo = CategoriaRepository()
        categoria = get_object_or_404(Categoria, id=id)
        nombre = request.POST.get('nombre')

        repo.update(
            categoria=categoria,
            nombre=nombre
        )
        return redirect('categoria-detail', categoria.id)

@method_decorator([login_required, staff_required], name='dispatch')
class CategoriaCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'categorias/create.html'
        )

    def post(self, request, *args, **kwargs):
        repo = CategoriaRepository()
        nombre = request.POST.get('nombre')

        nueva_categoria = repo.create(
            nombre=nombre
        )
        return redirect('categoria-detail', nueva_categoria.id)
