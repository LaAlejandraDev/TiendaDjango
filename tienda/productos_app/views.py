from django.shortcuts import render, get_object_or_404, redirect
from productos_app.models import Productos
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from . import forms

# Create your views here.
# Lista de los productos que se agregaron
class ListaProductosView(TemplateView):
    template_name = "lista_productos.html"
    def get_context_data(self):
        lista = Productos.objects.all()
        return {
            "lista": lista
        }
    
# Lista de los productos para cards
class CatalogoProductosView(TemplateView):
    template_name = 'catalogo_productos.html'

    def get_context_data(self):
        lista = Productos.objects.all()
        return {'lista': lista}
    
# Agregar prouctos
class CrearProductoView(FormView):
    template_name = "crear_producto.html"
    form_class = forms.ProductoRegistrarForms
    success_url = reverse_lazy('lista_productos')
    
    def  form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# Editar productos
class EditarProductoView(FormView):
    template_name = 'editar_producto.html'
    form_class = forms.ProductoEditarForms
    success_url = reverse_lazy('lista_productos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Productos, id=id)
        kwargs['instance'] = producto
        return kwargs
    
    def form_valid(self, form):
        form.save(self.kwargs.get('id'))
        return super().form_valid(form)