from django.contrib import admin



from .models import (
    Marca,
    ModeloAuto,
    Categoria,
    Auto,
    Cliente,
    Comentario,
    Venta,
    Empleado,
    Proveedor,
    Servicio,
    Cita,
    Inventario,
    Financiamiento,
    
)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    ordering = ('modelo', 'precio')
    search_fields = ('precio', 'modelo__nombre', 'categoria__nombre',)
    list_filter = ('categoria', 'modelo',)
    empty_value_display = "No hay datos para este campo"
    
    
    list_display = (
        'modelo',
        'precio',
        'descripcion',
        'categoria',
        'imagen',
    )

    fieldsets = [
        (
            "Info del Auto",
            {
                "fields" : ["modelo", "precio", "categoria"],
            }
        ),
        (
            "Info Extra",
            {
                "classes":["collapse"],
                "fields" : ["imagen", "descripcion"]
            }
        )
    ]




@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(ModeloAuto)
class ModeloAutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'direccion',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('auto', 'cliente_username', 'comentario', 'fecha',)

    def cliente_username(self, obj):
        return obj.cliente.user.username
    cliente_username.short_description = 'Cliente'



@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('auto', 'cliente', 'fecha', 'precio_final',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('user', 'puesto',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'direccion',)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio',)

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servicio', 'fecha', 'descripcion',)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('auto', 'cantidad', 'fecha_actualizacion',)

@admin.register(Financiamiento)
class FinanciamientoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'auto', 'monto_financiado', 'tasa_interes', 'plazo_meses', 'fecha_inicio', 'fecha_fin',)


    