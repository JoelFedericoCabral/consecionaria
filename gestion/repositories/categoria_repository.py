from typing import List, Optional
from gestion.models import Categoria

class CategoriaRepository:
    def get_all(self) -> List[Categoria]:
        return Categoria.objects.all()

    def get_by_id(self, id: int) -> Optional[Categoria]:
        return Categoria.objects.filter(id=id).first()

    def create(self, nombre: str) -> Categoria:
        return Categoria.objects.create(nombre=nombre)

    def delete(self, categoria: Categoria):
        return categoria.delete()
