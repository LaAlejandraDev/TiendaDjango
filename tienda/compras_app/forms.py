from django import forms
from compras_app.models import Compra
from productos_app.models import Productos

class CompraForms(forms.ModelForm):
    cantidad = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control w-100", 
            "placeholder": "Ingrese la cantidad"
        })
    )
    class Meta:
        model = Compra
        fields = ['cantidad']
    
    def save(self, id, user):
        producto = Productos.objects.get(id=id)
        compra = Compra(producto=producto, comprado_por=user, cantidad=self.cleaned_data['cantidad'])
        compra.save()
