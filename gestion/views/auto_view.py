from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.models import Auto, ModeloAuto, Comentario
from gestion.repositories.auto_repository import AutoRepository
from gestion.forms import AutoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from gestion.decorators import staff_required

class AutoListView(View):
    """
    Vista para listar todos los autos.

    Esta vista recupera todos los objetos de auto utilizando el repositorio AutoRepository 
    y los renderiza en una plantilla de lista de autos.
    """
    def get(self, request, *args, **kwargs):
        repo = AutoRepository()
        autos = repo.get_all()
        return render(request, 'autos/list.html', dict(autos=autos))

class AutoDetailView(View):
    """
    Vista para mostrar los detalles de un auto específico.

    Recupera un auto por su ID y muestra sus detalles junto con los comentarios asociados.
    """
    def get(self, request, id, *args, **kwargs):
        repo = AutoRepository()
        auto = get_object_or_404(Auto, id=id)
        comentarios = Comentario.objects.filter(auto=auto)
        return render(request, 'autos/detail.html', dict(auto=auto, comentarios=comentarios))

@method_decorator([login_required, staff_required], name='dispatch')
class AutoDeleteView(View):
    """
    Vista para eliminar un auto.

    Requiere que el usuario esté autenticado y tenga permisos de personal (staff).
    Solo permite peticiones POST para eliminar el auto.
    """
    def post(self, request, id, *args, **kwargs):
        repo = AutoRepository()
        auto = get_object_or_404(Auto, id=id)
        repo.delete(auto)
        return redirect('auto-list')

    def get(self, request, id, *args, **kwargs):
        """
        Método para manejar peticiones GET no permitidas.

        Retorna un HTTP 405 (Method Not Allowed) si se intenta acceder a la vista con un método GET.
        """
        return HttpResponseNotAllowed(['POST'])

@method_decorator([login_required, staff_required], name='dispatch')
class AutoUpdateView(View):
    """
    Vista para actualizar la información de un auto existente.

    Proporciona un formulario para editar los datos del auto y guarda los cambios
    si el formulario es válido.
    """
    def get(self, request, id, *args, **kwargs):
        """
        Maneja las peticiones GET para mostrar el formulario de actualización del auto.

        Renderiza la plantilla de actualización del auto con el formulario pre-llenado.
        """
        repo = AutoRepository()
        auto = get_object_or_404(Auto, id=id)
        form = AutoForm(instance=auto)
        return render(request, 'autos/update.html', {'form': form, 'auto': auto})

    def post(self, request, id, *args, **kwargs):
        """
        Maneja las peticiones POST para procesar el formulario de actualización del auto.

        Verifica la validez del formulario y guarda los cambios, redirigiendo a la vista de detalles
        del auto si tiene éxito.
        """
        repo = AutoRepository()
        auto = get_object_or_404(Auto, id=id)
        form = AutoForm(request.POST, request.FILES, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('auto-detail', auto.id)
        return render(request, 'autos/update.html', {'form': form, 'auto': auto})

@method_decorator([login_required, staff_required], name='dispatch')
class AutoCreateView(View):
    """
    Vista para crear un nuevo auto.

    Permite a los usuarios autenticados y con permisos de personal (staff) crear un nuevo auto
    mediante un formulario.
    """
    def get(self, request, *args, **kwargs):
        """
        Maneja las peticiones GET para mostrar el formulario de creación de autos.

        Renderiza la plantilla de creación de autos con el formulario vacío.
        """
        form = AutoForm()
        return render(request, 'autos/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Maneja las peticiones POST para procesar el formulario de creación de autos.

        Verifica la validez del formulario y guarda el nuevo auto, redirigiendo a la lista de autos si tiene éxito.
        """
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('auto-list')
        else:
            # Ajusta el queryset del campo 'modelo' si el campo 'marca' ha cambiado
            if 'marca' in request.POST:
                try:
                    marca_id = int(request.POST.get('marca'))
                    form.fields['modelo'].queryset = ModeloAuto.objects.filter(marca_id=marca_id).order_by('nombre')
                except (ValueError, TypeError):
                    form.fields['modelo'].queryset = ModeloAuto.objects.none()
        return render(request, 'autos/create.html', {'form': form})
