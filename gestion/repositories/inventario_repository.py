from typing import List, Optional
from gestion.models import Inventario, Auto

class InventarioRepository:
    def get_all(self) -> List[Inventario]:
        return Inventario.objects.all()

    def get_by_id(self, id: int) -> Optional[Inventario]:
        return Inventario.objects.filter(id=id).first()

    def create(self, auto: Auto, cantidad: int) -> Inventario:
        return Inventario.objects.create(auto=auto, cantidad=cantidad)

    def update(self, inventario: Inventario, cantidad: int) -> Inventario:
        inventario.cantidad = cantidad
        inventario.save()
        return inventario

    def delete(self, inventario: Inventario):
        return inventario.delete()