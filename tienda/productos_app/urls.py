from django.urls import path
from productos_app.views import ListaProductosView, CrearProductoView, EditarProductoView, CatalogoProductosView

urlpatterns = [
    path('lista_productos/', ListaProductosView.as_view(), name="lista_productos"),
    path('crear_producto/', CrearProductoView.as_view(), name="crear_producto"),
    path('editar_producto/<int:id>', EditarProductoView.as_view(), name="editar_producto"),
    path('catalogo_productos/', CatalogoProductosView.as_view(), name="catalogo_productos"),
]
