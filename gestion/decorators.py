from django.core.exceptions import PermissionDenied

def staff_required(view_func):
    """
    Decorador para vistas que requiere que el usuario tenga permisos de staff.

    Este decorador verifica si el usuario autenticado es miembro del staff.
    Si el usuario no es staff, se lanza una excepción PermissionDenied,
    denegando el acceso a la vista protegida.

    Args:
        view_func (function): La función de vista a proteger con el decorador.

    Returns:
        function: La función de vista decorada, que incluye la verificación de permisos.
    """
    def _wrapped_view_func(request, *args, **kwargs):
        # Verifica si el usuario autenticado es parte del staff.
        if not request.user.is_staff:
            # Si no es staff, se lanza una excepción de permiso denegado.
            raise PermissionDenied
        # Si es staff, continúa ejecutando la función de vista original.
        return view_func(request, *args, **kwargs)

    return _wrapped_view_func
