from typing import List, Optional
from gestion.models import Venta, Auto, Cliente

class VentaRepository:
    def get_all(self) -> List[Venta]:
        return Venta.objects.all()

    def get_by_id(self, id: int) -> Optional[Venta]:
        return Venta.objects.filter(id=id).first()

    def create(self, auto: Auto, cliente: Cliente, precio_final: float) -> Venta:
        return Venta.objects.create(auto=auto, cliente=cliente, precio_final=precio_final)

    def delete(self, venta: Venta):
        return venta.delete()
