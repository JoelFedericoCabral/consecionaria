from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.decorators import staff_required
from gestion.models import Financiamiento, Cliente, Auto
from gestion.repositories.financiamiento_repository import FinanciamientoRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class FinanciamientoListView(View):
    def get(self, request, *args, **kwargs):
        repo = FinanciamientoRepository()
        financiamentos = repo.get_all()
        return render(
            request,
            'financiamientos/list.html',
            dict(
                financiamentos=financiamentos
            )
        )

class FinanciamientoDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = FinanciamientoRepository()
        financiamiento = get_object_or_404(Financiamiento, id=id)
        return render(
            request,
            'financiamientos/detail.html',
            dict(
                financiamiento=financiamiento
            )
        )

class FinanciamientoDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = FinanciamientoRepository()
        financiamiento = get_object_or_404(Financiamiento, id=id)
        repo.delete(financiamiento)
        return redirect('financiamiento-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator(login_required, name='dispatch')
class FinanciamientoUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = FinanciamientoRepository()
        financiamiento = get_object_or_404(Financiamiento, id=id)
        autos = Auto.objects.all()
        clientes = Cliente.objects.all()
        return render(
            request,
            'financiamientos/update.html',
            dict(
                financiamiento=financiamiento,
                autos=autos,
                clientes=clientes
            )
        )

    def post(self, request, id, *args, **kwargs):
        repo = FinanciamientoRepository()
        financiamiento = get_object_or_404(Financiamiento, id=id)
        auto = get_object_or_404(Auto, id=request.POST.get('auto_id'))
        cliente = get_object_or_404(Cliente, id=request.POST.get('cliente_id'))
        monto_financiado = request.POST.get('monto_financiado')
        tasa_interes = request.POST.get('tasa_interes')
        plazo_meses = request.POST.get('plazo_meses')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        repo.update(
            financiamiento=financiamiento,
            auto=auto,
            cliente=cliente,
            monto_financiado=monto_financiado,
            tasa_interes=tasa_interes,
            plazo_meses=plazo_meses,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        return redirect('financiamiento-detail', financiamiento.id)


@method_decorator([login_required, staff_required], name='dispatch')
class FinanciamientoCreateView(View):
    def get(self, request, *args, **kwargs):
        autos = Auto.objects.all()
        clientes = Cliente.objects.all()
        return render(
            request,
            'financiamientos/create.html',
            dict(
                autos=autos,
                clientes=clientes
            )
        )

    def post(self, request, *args, **kwargs):
        repo = FinanciamientoRepository()
        auto = get_object_or_404(Auto, id=request.POST.get('auto_id'))
        cliente = get_object_or_404(Cliente, id=request.POST.get('cliente_id'))
        monto_financiado = request.POST.get('monto_financiado')
        tasa_interes = request.POST.get('tasa_interes')
        plazo_meses = request.POST.get('plazo_meses')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        nuevo_financiamiento = repo.create(
            auto=auto,
            cliente=cliente,
            monto_financiado=monto_financiado,
            tasa_interes=tasa_interes,
            plazo_meses=plazo_meses,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        return redirect('financiamiento-detail', nuevo_financiamiento.id)
