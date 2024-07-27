from typing import List, Optional
from gestion.models import Cliente
from django.contrib.auth.models import User

class ClienteRepository:
    def get_all(self) -> List[Cliente]:
        return Cliente.objects.all()

    def get_by_id(self, id: int) -> Optional[Cliente]:
        return Cliente.objects.filter(id=id).first()

    def create(self, user: User, telefono: str, direccion: str) -> Cliente:
        return Cliente.objects.create(user=user, telefono=telefono, direccion=direccion)

    def delete(self, cliente: Cliente):
        return cliente.delete()
