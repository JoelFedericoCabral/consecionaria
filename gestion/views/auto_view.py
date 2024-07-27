from django.http import HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from gestion.models import Auto, ModeloAuto, Categoria
from gestion.repositories.auto_repository import AutoRepository
from gestion.forms import AutoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from gestion.decorators import staff_required

class AutoListView(View):
    def get(self, request, *args, **kwargs):
        repo = AutoRepository()
        autos = repo.get_all()
        return render(request, 'autos/list.html', dict(autos=autos))

class AutoDetailView(View):
    def get(self, request, id, *args, **kwargs):
        repo = AutoRepository()
        auto = get_object_or_404(Auto, id=id)
        return render(request, 'autos/detail.html', dict(auto=auto))

@method_decorator([login_required, staff_required], name='dispatch')
class AutoDeleteView(View):
    def post(self, request, id, *args, **kwargs):
        repo = AutoRepository()
        auto = get_object_or_404(Auto, id=id)
        repo.delete(auto)
        return redirect('auto-list')

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@method_decorator([login_required, staff_required], name='dispatch')
class AutoUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        repo = AutoRepository()
        auto = get_object_or_404(Auto, id=id)
        form = AutoForm(instance=auto)
        return render(request, 'autos/update.html', {'form': form, 'auto': auto})

    def post(self, request, id, *args, **kwargs):
        repo = AutoRepository()
        auto = get_object_or_404(Auto, id=id)
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('auto-detail', auto.id)
        return render(request, 'autos/update.html', {'form': form, 'auto': auto})

@method_decorator([login_required, staff_required], name='dispatch')
class AutoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = AutoForm()
        return render(request, 'autos/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('auto-list')
        else:
            if 'marca' in request.POST:
                try:
                    marca_id = int(request.POST.get('marca'))
                    form.fields['modelo'].queryset = ModeloAuto.objects.filter(marca_id=marca_id).order_by('nombre')
                except (ValueError, TypeError):
                    form.fields['modelo'].queryset = ModeloAuto.objects.none()
        return render(request, 'autos/create.html', {'form': form})