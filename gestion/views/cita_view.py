from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Cita, Cliente, Servicio
from gestion.repositories.cita_repository import CitaRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CitaListView(View):
    def get(self, request, *args, **kwargs):
        repo = CitaRepository()
        citas = repo.get_all()
        return render(
            request,
            'citas/list.html',
            dict(
                citas=citas
            )
        )

class CitaDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = CitaRepository()
        cita = get_object_or_404(Cita, id=id)
        return render(
            request,
            'citas/detail.html',
            dict(
                cita=cita
            )
        )

class CitaDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = CitaRepository()
        cita = get_object_or_404(Cita, id=id)
        repo.delete(cita)
        return redirect('cita-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class CitaUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = CitaRepository()
        cita = get_object_or_404(Cita, id=id)
        clientes = Cliente.objects.all()
        servicios = Servicio.objects.all()
        return render(
            request,
            'citas/update.html',
            dict(
                cita=cita,
                clientes=clientes,
                servicios=servicios
            )
        )

    def post(self, request, id, *args, **kwargs):
        repo = CitaRepository()
        cita = get_object_or_404(Cita, id=id)
        cliente = get_object_or_404(Cliente, id=request.POST.get('cliente_id'))
        servicio = get_object_or_404(Servicio, id=request.POST.get('servicio_id'))
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')

        repo.update(
            cita=cita,
            cliente=cliente,
            servicio=servicio,
            descripcion=descripcion,
            fecha=fecha
        )
        return redirect('cita-detail', cita.id)


@method_decorator([login_required, staff_required], name='dispatch')
class CitaCreateView(View):
    def get(self, request, *args, **kwargs):
        clientes = Cliente.objects.all()
        servicios = Servicio.objects.all()
        return render(
            request,
            'citas/create.html',
            dict(
                clientes=clientes,
                servicios=servicios
            )
        )

    def post(self, request, *args, **kwargs):
        repo = CitaRepository()
        cliente = get_object_or_404(Cliente, id=request.POST.get('cliente_id'))
        servicio = get_object_or_404(Servicio, id=request.POST.get('servicio_id'))
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')

        nueva_cita = repo.create(
            cliente=cliente,
            servicio=servicio,
            descripcion=descripcion,
            fecha=fecha
        )
        return redirect('cita-detail', nueva_cita.id)
