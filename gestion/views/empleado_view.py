from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Empleado
from gestion.repositories.empleado_repository import EmpleadoRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class EmpleadoListView(View):
    def get(self, request, *args, **kwargs):
        repo = EmpleadoRepository()
        empleados = repo.get_all()
        return render(
            request,
            'empleados/list.html',
            dict(
                empleados=empleados
            )
        )

class EmpleadoDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = EmpleadoRepository()
        empleado = get_object_or_404(Empleado, id=id)
        return render(
            request,
            'empleados/detail.html',
            dict(
                empleado=empleado
            )
        )

class EmpleadoDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = EmpleadoRepository()
        empleado = get_object_or_404(Empleado, id=id)
        repo.delete(empleado)
        return redirect('empleado-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class EmpleadoUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = EmpleadoRepository()
        empleado = get_object_or_404(Empleado, id=id)
        return render(
            request,
            'empleados/update.html',
            dict(empleado=empleado)
        )

    def post(self, request, id, *args, **kwargs):
        repo = EmpleadoRepository()
        empleado = get_object_or_404(Empleado, id=id)
        puesto = request.POST.get('puesto')

        repo.update(
            empleado=empleado,
            puesto=puesto
        )
        return redirect('empleado-detail', empleado.id)

@method_decorator([login_required, staff_required], name='dispatch')
class EmpleadoCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'empleados/create.html'
        )

    def post(self, request, *args, **kwargs):
        repo = EmpleadoRepository()
        user = request.user
        puesto = request.POST.get('puesto')

        nuevo_empleado = repo.create(
            user=user,
            puesto=puesto
        )
        return redirect('empleado-detail', nuevo_empleado.id)
