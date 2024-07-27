from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Servicio
from gestion.repositories.servicio_repository import ServicioRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ServicioListView(View):
    def get(self, request, *args, **kwargs):
        repo = ServicioRepository()
        servicios = repo.get_all()
        return render(
            request,
            'servicios/list.html',
            dict(
                servicios=servicios
            )
        )

class ServicioDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ServicioRepository()
        servicio = get_object_or_404(Servicio, id=id)
        return render(
            request,
            'servicios/detail.html',
            dict(
                servicio=servicio
            )
        )

class ServicioDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = ServicioRepository()
        servicio = get_object_or_404(Servicio, id=id)
        repo.delete(servicio)
        return redirect('servicio-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class ServicioUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = ServicioRepository()
        servicio = get_object_or_404(Servicio, id=id)
        return render(
            request,
            'servicios/update.html',
            dict(servicio=servicio)
        )

    def post(self, request, id, *args, **kwargs):
        repo = ServicioRepository()
        servicio = get_object_or_404(Servicio, id=id)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')

        repo.update(
            servicio=servicio,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio
        )
        return redirect('servicio-detail', servicio.id)


@method_decorator([login_required, staff_required], name='dispatch')
class ServicioCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'servicios/create.html'
        )

    def post(self, request, *args, **kwargs):
        repo = ServicioRepository()
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')

        nuevo_servicio = repo.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio
        )
        return redirect('servicio-detail', nuevo_servicio.id)
