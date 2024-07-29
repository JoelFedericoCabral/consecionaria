from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.forms import ComentarioForm
from gestion.models import Comentario
from gestion.repositories.comentario_repository import ComentarioRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

class ComentarioListView(View):
    def get(self, request, *args, **kwargs):
        repo = ComentarioRepository()
        comentarios = repo.get_all()
        return render(
            request,
            'comentarios/list.html',
            dict(
                comentarios=comentarios
            )
        )

class ComentarioDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ComentarioRepository()
        comentario = get_object_or_404(Comentario, id=id)
        return render(
            request,
            'comentarios/detail.html',
            dict(
                comentario=comentario
            )
        )

@method_decorator(login_required, name='dispatch')
class ComentarioDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        comentario = get_object_or_404(Comentario, id=id)

        if not request.user.is_staff and request.user != comentario.autor:
            messages.error(request, '<span style="color: red;">No tienes permiso para eliminar este comentario.</span>')
            return redirect('comentario-detail', id=id)

        repo = ComentarioRepository()
        repo.delete(comentario)
        return redirect('comentario-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class ComentarioUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ComentarioRepository()
        comentario = get_object_or_404(Comentario, id=id)

        if request.user != comentario.autor:
            messages.error(request, '<span style="color: red;">No tienes permiso para editar este comentario.</span>')
            return redirect('comentario-detail', id=id)

        form = ComentarioForm(instance=comentario)
        return render(
            request,
            'comentarios/update.html',
            dict(form=form)
        )

    def post(self, request, id, *args, **kwargs):
        repo = ComentarioRepository()
        comentario = get_object_or_404(Comentario, id=id)

        if request.user != comentario.autor:
            messages.error(request, '<span style="color: red;">No tienes permiso para editar este comentario.</span>')
            return redirect('comentario-detail', id=id)

        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('comentario-detail', comentario.id)
        return render(
            request,
            'comentarios/update.html',
            dict(form=form)
        )

class ComentarioCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ComentarioForm()
        return render(
            request,
            'comentarios/create.html',
            dict(
                form=form
            )
        )

    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.save()
            return redirect('comentario-detail', comentario.id)
        return render(
            request,
            'comentarios/create.html',
            dict(
                form=form
            )
        )