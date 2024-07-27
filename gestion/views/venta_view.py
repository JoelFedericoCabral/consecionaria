from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Venta, Auto, Cliente
from gestion.repositories.venta_repository import VentaRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class VentaListView(View):
    def get(self, request, *args, **kwargs):
        repo = VentaRepository()
        ventas = repo.get_all()
        return render(
            request,
            'ventas/list.html',
            dict(
                ventas=ventas
            )
        )

class VentaDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = VentaRepository()
        venta = get_object_or_404(Venta, id=id)
        return render(
            request,
            'ventas/detail.html',
            dict(
                venta=venta
            )
        )

class VentaDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = VentaRepository()
        venta = get_object_or_404(Venta, id=id)
        repo.delete(venta)
        return redirect('venta-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class VentaUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = VentaRepository()
        venta = get_object_or_404(Venta, id=id)
        autos = Auto.objects.all()
        clientes = Cliente.objects.all()
        return render(
            request,
            'ventas/update.html',
            dict(
                venta=venta,
                autos=autos,
                clientes=clientes
            )
        )

    def post(self, request, id, *args, **kwargs):
        repo = VentaRepository()
        venta = get_object_or_404(Venta, id=id)
        auto = get_object_or_404(Auto, id=request.POST.get('auto_id'))
        cliente = get_object_or_404(Cliente, id=request.POST.get('cliente_id'))
        precio_final = request.POST.get('precio_final')

        repo.update(
            venta=venta,
            auto=auto,
            cliente=cliente,
            precio_final=precio_final
        )
        return redirect('venta-detail', venta.id)


@method_decorator([login_required, staff_required], name='dispatch')
class VentaCreateView(View):
    def get(self, request, *args, **kwargs):
        autos = Auto.objects.all()
        clientes = Cliente.objects.all()
        return render(
            request,
            'ventas/create.html',
            dict(
                autos=autos,
                clientes=clientes
            )
        )

    def post(self, request, *args, **kwargs):
        repo = VentaRepository()
        auto = get_object_or_404(Auto, id=request.POST.get('auto_id'))
        cliente = get_object_or_404(Cliente, id=request.POST.get('cliente_id'))
        precio_final = request.POST.get('precio_final')

        nueva_venta = repo.create(
            auto=auto,
            cliente=cliente,
            precio_final=precio_final
        )
        return redirect('venta-detail', nueva_venta.id)
