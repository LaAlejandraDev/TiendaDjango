from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from . import forms
from productos_app.models import Productos
from compras_app.models import Compra
from django.contrib.auth.models import User

# View de las compras de los usarios que no son admin
class ListadoComprasUsuarioView(TemplateView):
    template_name = 'lista_compras.html'

    def get_context_data(self, **kwargs): #Enviar datos al template 
        context = super().get_context_data(**kwargs)
        comprador = self.request.user #obtener el usuario que hace compras
        lista = Compra.objects.filter(comprado_por=comprador)
        context['lista']=lista
        return context

# View del administrador, donde el puede ver todas las ventas de los usuarios
class ListadoComprasAdminView(TemplateView):
    template_name = "lista_compras_admin.html"
    
    def get_context_data(self):
        lista = Compra.objects.all()
        return {
            "lista": lista
        }


# View para las cards
class ComprarProductoView(FormView):
    template_name = "comprar_producto.html"
    form_class = forms.CompraForms
    success_url = reverse_lazy('catalogo_productos')
    
    #Obtenemos la información de cada productos en las cards
    def get_context_data(self):
        kwargs = super().get_context_data()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Productos, id=id)
        kwargs['producto'] = producto
        return kwargs

    
    #Obtenemos los datos para inicializar el formulario de la persona que compra un producto
    def get_kwargs_data(self):
        kwargs = super().get_kwargs_data()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Productos, id=id)
        kwargs['instance'] = Compra(producto=producto, cliente =self.request.user)
        return kwargs
    
    def form_valid(self, form):
        form.save(self.kwargs.get('id'), user = self.request.user)
        return super().form_valid(form)
    
    