from django import forms 
from productos_app.models import Productos

class ProductoRegistrarForms(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['producto_nombre', 'producto_precio', 'producto_imagen']
        widgets = {
            "producto_nombre": forms.TextInput(attrs={"class": "form-control w-100", "placeholder": "Ingrese el nombre del producto"}),
            "producto_precio": forms.NumberInput(attrs={"class": "form-control w-100", "placeholder": "Ingrese el precio"}),
            "producto_imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
    
class ProductoEditarForms(forms.ModelForm):
    producto_nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control w-100", 
            "placeholder": "Ingrese el nombre del producto"
        })
    )
    producto_precio = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control w-100", 
            "placeholder": "Ingrese el precio del producto"
        })
    )
    producto_imagen = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control"
        })
    )

    class Meta:
        model = Productos
        fields = ['producto_nombre', 'producto_precio', 'producto_imagen']
    def save(self, id):
        producto = Productos.objects.filter(id=id).first()
        producto.producto_nombre = self.cleaned_data['producto_nombre']
        producto.producto_precio = self.cleaned_data['producto_precio']
        producto.producto_imagen = self.cleaned_data['producto_imagen']
        producto.save()
        
