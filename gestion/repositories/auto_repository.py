from typing import List, Optional
from gestion.models import Auto, ModeloAuto, Categoria

class AutoRepository:
    def get_all(self) -> List[Auto]:
        return Auto.objects.all()

    def get_by_id(self, id: int) -> Optional[Auto]:
        return Auto.objects.filter(id=id).first()

    def create(self, modelo: ModeloAuto, categoria: Categoria, precio: float, imagen, descripcion: str) -> Auto:
        return Auto.objects.create(modelo=modelo, categoria=categoria, precio=precio, imagen=imagen, descripcion=descripcion)

    def delete(self, auto: Auto):
        return auto.delete()

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Auto]:
        return Auto.objects.filter(precio__range=(min_price, max_price))

    def get_modelos_by_marca(self, marca_id: int) -> List[ModeloAuto]:
        return ModeloAuto.objects.filter(marca_id=marca_id).order_by('nombre')
