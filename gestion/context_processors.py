from gestion.models import Marca, Categoria
from django.core.cache import cache

def user_info(request):
    """
    Añade información del usuario autenticado al contexto.

    Este context processor proporciona el usuario autenticado al contexto 
    de las plantillas si el usuario está autenticado. De lo contrario, devuelve None.

    Args:
        request: Objeto HttpRequest que contiene los detalles de la solicitud.

    Returns:
        Un diccionario con la clave 'authenticated_user' que contiene el objeto usuario autenticado o None.
    """
    user = request.user if request.user.is_authenticated else None
    return {
        'authenticated_user': user
    }

def all_brands(request):
    """
    Añade todas las marcas al contexto.

    Este context processor obtiene todas las marcas de la base de datos y las 
    almacena en caché para mejorar el rendimiento. Si las marcas no están en 
    caché, las recupera de la base de datos y las almacena por 10 horas.

    Args:
        request: Objeto HttpRequest que contiene los detalles de la solicitud.

    Returns:
        Un diccionario con la clave 'all_brands' que contiene un queryset de objetos Marca.
    """
    brands = cache.get('brands')
    if brands is None:
        brands = Marca.objects.all()
        cache.set('brands', brands, 36000)  # Cache por 10 horas (36000 segundos)
    return {'all_brands': brands}

def all_categories(request):
    """
    Añade todas las categorías al contexto.

    Este context processor obtiene todas las categorías de la base de datos y las 
    almacena en caché para mejorar el rendimiento. Si las categorías no están en 
    caché, las recupera de la base de datos y las almacena por 10 horas.

    Args:
        request: Objeto HttpRequest que contiene los detalles de la solicitud.

    Returns:
        Un diccionario con la clave 'all_categories' que contiene un queryset de objetos Categoria.
    """
    categories = cache.get('categories')
    if categories is None:
        categories = Categoria.objects.all()  # Devuelve objetos completos
        cache.set('categories', categories, 36000)  # Cache por 10 horas (36000 segundos)
    return {'all_categories': categories}
