from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):
    producto_nombre = models.TextField(max_length=100)
    producto_precio = models.FloatField(max_length=100)
    producto_imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    class Meta: 
        permissions = [("poder_agregar_productos", "Puede usar crud productos")]
        ordering = ['producto_nombre']
        
        
    def __str__(self):
        return f"{self.id}-{self.producto_nombre}"