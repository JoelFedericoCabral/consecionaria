from django.urls import path
from .views import (
    auto_view, cliente_view, marca_view, modelo_auto_view,
    categoria_view, comentario_view, venta_view, empleado_view,
    proveedor_view, servicio_view, cita_view, inventario_view, financiamiento_view,
)

urlpatterns = [
    path('autos/', auto_view.AutoListView.as_view(), name='auto-list'),
    path('autos/<int:id>/', auto_view.AutoDetailView.as_view(), name='auto-detail'),
    path('autos/nuevo/', auto_view.AutoCreateView.as_view(), name='auto-create'),
    path('autos/<int:id>/editar/', auto_view.AutoUpdateView.as_view(), name='auto-update'),
    path('autos/<int:id>/eliminar/', auto_view.AutoDeleteView.as_view(), name='auto-delete'),
    
    path('clientes/', cliente_view.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:id>/', cliente_view.ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/<int:id>/delete/', cliente_view.ClienteDeleteView.as_view(), name='cliente-delete'),
    path('clientes/<int:id>/update/', cliente_view.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/create/', cliente_view.ClienteCreateView.as_view(), name='cliente-create'),

    path('marcas/', marca_view.MarcaListView.as_view(), name='marca-list'),
    path('marcas/<int:id>/', marca_view.MarcaDetailView.as_view(), name='marca-detail'),
    path('marcas/<int:id>/delete/', marca_view.MarcaDeleteView.as_view(), name='marca-delete'),
    path('marcas/<int:id>/update/', marca_view.MarcaUpdateView.as_view(), name='marca-update'),
    path('marcas/create/', marca_view.MarcaCreateView.as_view(), name='marca-create'),

    path('modelos/', modelo_auto_view.ModeloAutoListView.as_view(), name='modelo-list'),
    path('modelos/<int:id>/', modelo_auto_view.ModeloAutoDetailView.as_view(), name='modelo-detail'),
    path('modelos/<int:id>/delete/', modelo_auto_view.ModeloAutoDeleteView.as_view(), name='modelo-delete'),
    path('modelos/<int:id>/update/', modelo_auto_view.ModeloAutoUpdateView.as_view(), name='modelo-update'),
    path('modelos/create/', modelo_auto_view.ModeloAutoCreateView.as_view(), name='modelo-create'),

    path('categorias/', categoria_view.CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:id>/', categoria_view.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categorias/<int:id>/delete/', categoria_view.CategoriaDeleteView.as_view(), name='categoria-delete'),
    path('categorias/<int:id>/update/', categoria_view.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/create/', categoria_view.CategoriaCreateView.as_view(), name='categoria-create'),

    path('comentarios/', comentario_view.ComentarioListView.as_view(), name='comentario-list'),
    path('comentarios/<int:id>/', comentario_view.ComentarioDetailView.as_view(), name='comentario-detail'),
    path('comentarios/<int:id>/delete/', comentario_view.ComentarioDeleteView.as_view(), name='comentario-delete'),
    path('comentarios/<int:id>/update/', comentario_view.ComentarioUpdateView.as_view(), name='comentario-update'),
    path('comentarios/create/', comentario_view.ComentarioCreateView.as_view(), name='comentario-create'),

    path('ventas/', venta_view.VentaListView.as_view(), name='venta-list'),
    path('ventas/<int:id>/', venta_view.VentaDetailView.as_view(), name='venta-detail'),
    path('ventas/<int:id>/delete/', venta_view.VentaDeleteView.as_view(), name='venta-delete'),
    path('ventas/<int:id>/update/', venta_view.VentaUpdateView.as_view(), name='venta-update'),
    path('ventas/create/', venta_view.VentaCreateView.as_view(), name='venta-create'),

    path('empleados/', empleado_view.EmpleadoListView.as_view(), name='empleado-list'),
    path('empleados/<int:id>/', empleado_view.EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('empleados/<int:id>/delete/', empleado_view.EmpleadoDeleteView.as_view(), name='empleado-delete'),
    path('empleados/<int:id>/update/', empleado_view.EmpleadoUpdateView.as_view(), name='empleado-update'),
    path('empleados/create/', empleado_view.EmpleadoCreateView.as_view(), name='empleado-create'),

    path('proveedores/', proveedor_view.ProveedorListView.as_view(), name='proveedor-list'),
    path('proveedores/<int:id>/', proveedor_view.ProveedorDetailView.as_view(), name='proveedor-detail'),
    path('proveedores/<int:id>/delete/', proveedor_view.ProveedorDeleteView.as_view(), name='proveedor-delete'),
    path('proveedores/<int:id>/update/', proveedor_view.ProveedorUpdateView.as_view(), name='proveedor-update'),
    path('proveedores/create/', proveedor_view.ProveedorCreateView.as_view(), name='proveedor-create'),

    path('servicios/', servicio_view.ServicioListView.as_view(), name='servicio-list'),
    path('servicios/<int:id>/', servicio_view.ServicioDetailView.as_view(), name='servicio-detail'),
    path('servicios/<int:id>/delete/', servicio_view.ServicioDeleteView.as_view(), name='servicio-delete'),
    path('servicios/<int:id>/update/', servicio_view.ServicioUpdateView.as_view(), name='servicio-update'),
    path('servicios/create/', servicio_view.ServicioCreateView.as_view(), name='servicio-create'),

    path('citas/', cita_view.CitaListView.as_view(), name='cita-list'),
    path('citas/<int:id>/', cita_view.CitaDetailView.as_view(), name='cita-detail'),
    path('citas/<int:id>/delete/', cita_view.CitaDeleteView.as_view(), name='cita-delete'),
    path('citas/<int:id>/update/', cita_view.CitaUpdateView.as_view(), name='cita-update'),
    path('citas/create/', cita_view.CitaCreateView.as_view(), name='cita-create'),

    path('inventario/', inventario_view.InventarioListView.as_view(), name='inventario-list'),
    path('inventario/<int:id>/', inventario_view.InventarioDetailView.as_view(), name='inventario-detail'),
    path('inventario/<int:id>/delete/', inventario_view.InventarioDeleteView.as_view(), name='inventario-delete'),
    path('inventario/<int:id>/update/', inventario_view.InventarioUpdateView.as_view(), name='inventario-update'),
    path('inventario/create/', inventario_view.InventarioCreateView.as_view(), name='inventario-create'),

    path('financiamiento/', financiamiento_view.FinanciamientoListView.as_view(), name='financiamiento-list'),
    path('financiamiento/<int:id>/', financiamiento_view.FinanciamientoDetailView.as_view(), name='financiamiento-detail'),
    path('financiamiento/<int:id>/delete/', financiamiento_view.FinanciamientoDeleteView.as_view(), name='financiamiento-delete'),
    path('financiamiento/<int:id>/update/', financiamiento_view.FinanciamientoUpdateView.as_view(), name='financiamiento-update'),
    path('financiamiento/create/', financiamiento_view.FinanciamientoCreateView.as_view(), name='financiamiento-create'),
]