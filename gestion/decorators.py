from django.core.exceptions import PermissionDenied

def staff_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func
