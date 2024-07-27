from typing import List, Optional
from gestion.models import Empleado
from django.contrib.auth.models import User

class EmpleadoRepository:
    def get_all(self) -> List[Empleado]:
        return Empleado.objects.all()

    def get_by_id(self, id: int) -> Optional[Empleado]:
        return Empleado.objects.filter(id=id).first()

    def create(self, user: User, puesto: str) -> Empleado:
        return Empleado.objects.create(user=user, puesto=puesto)

    def delete(self, empleado: Empleado):
        return empleado.delete()
