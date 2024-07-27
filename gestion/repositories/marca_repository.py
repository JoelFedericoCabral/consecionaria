from typing import List, Optional
from gestion.models import Marca

class MarcaRepository:
    def get_all(self) -> List[Marca]:
        return Marca.objects.all()

    def get_by_id(self, id: int) -> Optional[Marca]:
        return Marca.objects.filter(id=id).first()

    def create(self, nombre: str) -> Marca:
        return Marca.objects.create(nombre=nombre)

    def delete(self, marca: Marca):
        return marca.delete()
