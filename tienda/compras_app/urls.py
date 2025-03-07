from django.urls import path
from compras_app.views import ComprarProductoView, ListadoComprasUsuarioView, ListadoComprasAdminView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('comprar_productos/<int:id>', login_required(ComprarProductoView.as_view()), name='comprar_productos'),
    path('listado_compras_usuarios/<int:id>', login_required(ListadoComprasUsuarioView.as_view()), name='listado_compras_usuarios'),
    path('listado_compras_admin/', ListadoComprasAdminView.as_view(), name='listado_compras_admin'),
]