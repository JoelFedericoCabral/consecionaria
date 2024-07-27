from typing import List, Optional
from gestion.models import ModeloAuto, Marca

class ModeloAutoRepository:
    def get_all(self) -> List[ModeloAuto]:
        return ModeloAuto.objects.all()

    def get_by_id(self, id: int) -> Optional[ModeloAuto]:
        return ModeloAuto.objects.filter(id=id).first()

    def create(self, marca: Marca, nombre: str) -> ModeloAuto:
        return ModeloAuto.objects.create(marca=marca, nombre=nombre)

    def delete(self, modelo_auto: ModeloAuto):
        return modelo_auto.delete()
