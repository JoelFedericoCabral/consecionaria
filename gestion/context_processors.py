from gestion.models import Marca, Categoria
from django.core.cache import cache

def user_info(request):
    user = request.user if request.user.is_authenticated else None
    return {
        'authenticated_user': user
    }

def all_brands(request):
    brands = cache.get('brands')
    if brands is None:
        brands = Marca.objects.all()
        cache.set('brands', brands, 36000) 
    return {'all_brands': brands}

def all_categories(request):
    categories = cache.get('categories')
    if categories is None:
        categories = Categoria.objects.all()  # Return full objects
        cache.set('categories', categories, 36000)
    return {'all_categories': categories}