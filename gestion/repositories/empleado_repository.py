from typing import List, Optional
from gestion.models import Empleado
from django.contrib.auth.models import User

class EmpleadoRepository:
    def get_all(self) -> List[Empleado]:
        return Empleado.objects.all()

    def get_by_id(self, id: int) -> Optional[Empleado]:
        return Empleado.objects.filter(id=id).first()

    def create(self, user: User, nombre: str, apellido: str, telefono: str, dni: str, direccion: str, puesto: str) -> Empleado:
        return Empleado.objects.create(
            user=user,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            dni=dni,
            direccion=direccion,
            puesto=puesto
        )

    def update(self, empleado: Empleado, nombre: str, apellido: str, telefono: str, dni: str, direccion: str, puesto: str) -> Empleado:
        empleado.nombre = nombre
        empleado.apellido = apellido
        empleado.telefono = telefono
        empleado.dni = dni
        empleado.direccion = direccion
        empleado.puesto = puesto
        empleado.save()
        return empleado

    def delete(self, empleado: Empleado):
        return empleado.delete()
