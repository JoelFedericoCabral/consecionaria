from typing import List, Optional
from gestion.models import Comentario, Auto, Cliente

class ComentarioRepository:
    def get_all(self) -> List[Comentario]:
        return Comentario.objects.all()

    def get_by_id(self, id: int) -> Optional[Comentario]:
        return Comentario.objects.filter(id=id).first()

    def create(self, auto: Auto, cliente: Cliente, comentario: str) -> Comentario:
        return Comentario.objects.create(auto=auto, cliente=cliente, comentario=comentario)

    def delete(self, comentario: Comentario):
        return comentario.delete()
