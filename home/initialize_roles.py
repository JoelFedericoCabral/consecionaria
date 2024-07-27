from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from gestion.models import Comentario

class Command(BaseCommand):
    help = 'Create initial user roles and permissions'

    def handle(self, *args, **kwargs):
        # Crear grupo staff
        staff_group, created = Group.objects.get_or_create(name='staff')

        # Crear grupo usuarios
        usuario_group, created = Group.objects.get_or_create(name='usuarios')

        # Asignar permisos a grupo staff
        content_type = ContentType.objects.get_for_model(Comentario)
        permission = Permission.objects.get(
            codename='delete_comentario',
            content_type=content_type,
        )
        staff_group.permissions.add(permission)

        # Asignar permisos a grupo usuarios (crear, editar, eliminar sus propios comentarios)
        usuario_permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=['add_comentario', 'change_comentario', 'delete_comentario']
        )
        for perm in usuario_permissions:
            usuario_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Roles and permissions have been initialized'))
