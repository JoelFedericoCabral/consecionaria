from typing import List, Optional
from gestion.models import Financiamiento, Auto, Cliente




class FinanciamientoRepository:
    def get_all(self) -> List[Financiamiento]:
        return Financiamiento.objects.all()

    def get_by_id(self, id: int) -> Optional[Financiamiento]:
        return Financiamiento.objects.filter(id=id).first()

    def create(self, cliente: Cliente, auto: Auto, monto_financiado: float, tasa_interes: float, plazo_meses: int, fecha_inicio, fecha_fin) -> Financiamiento:
        return Financiamiento.objects.create(cliente=cliente, auto=auto, monto_financiado=monto_financiado, tasa_interes=tasa_interes, plazo_meses=plazo_meses, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)

    def update(self, financiamiento: Financiamiento, monto_financiado: float, tasa_interes: float, plazo_meses: int, fecha_inicio, fecha_fin) -> Financiamiento:
        financiamiento.monto_financiado = monto_financiado
        financiamiento.tasa_interes = tasa_interes
        financiamiento.plazo_meses = plazo_meses
        financiamiento.fecha_inicio = fecha_inicio
        financiamiento.fecha_fin = fecha_fin
        financiamiento.save()
        return financiamiento

    def delete(self, financiamiento: Financiamiento):
        return financiamiento.delete()