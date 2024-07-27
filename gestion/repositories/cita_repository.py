from typing import List, Optional
from gestion.models import Cita, Cliente, Servicio

class CitaRepository:
    def get_all(self) -> List[Cita]:
        return Cita.objects.all()

    def get_by_id(self, id: int) -> Optional[Cita]:
        return Cita.objects.filter(id=id).first()

    def create(self, cliente: Cliente, servicio: Servicio, fecha, descripcion: str) -> Cita:
        return Cita.objects.create(cliente=cliente, servicio=servicio, fecha=fecha, descripcion=descripcion)

    def delete(self, cita: Cita):
        return cita.delete()
