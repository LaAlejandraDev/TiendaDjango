from django.contrib.auth.models import User
from django.db import models
from productos_app.models import Productos

class Compra(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, default=1)
    cantidad = models.IntegerField(default=1)
    comprado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='producto_comprado_user')
    
    def __str__(self):
        return f"Comprado por{self.comprado_por}"
