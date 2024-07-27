from typing import List, Optional
from gestion.models import Proveedor

class ProveedorRepository:
    def get_all(self) -> List[Proveedor]:
        return Proveedor.objects.all()

    def get_by_id(self, id: int) -> Optional[Proveedor]:
        return Proveedor.objects.filter(id=id).first()

    def create(self, nombre: str, telefono: str, direccion: str) -> Proveedor:
        return Proveedor.objects.create(nombre=nombre, telefono=telefono, direccion=direccion)

    def delete(self, proveedor: Proveedor):
        return proveedor.delete()
