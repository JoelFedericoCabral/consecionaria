from gestion.models import Marca, Categoria

def user_info(request):
    user = request.user if request.user.is_authenticated else None
    return {
        'authenticated_user': user
    }

def all_brands(request):
    brands = Marca.objects.all().values_list('nombre', flat=True)
    return {
        'all_brands': brands
    }

def all_categories(request):
    categories = Categoria.objects.all().values_list('nombre', flat=True)
    return {
        'all_categories': categories
    }
