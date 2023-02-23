from django.db import models

class Productos(models.Model):
    producto_nombre=models.CharField(max_length=100)
    producto_descripcion=models.TextField(blank=True,null=True)
    producto_imagen=models.CharField(max_length=120,blank=True,null=True)
    producto_precio=models.DecimalField(max_digits=7,decimal_places=2)
    producto_estado=models.BooleanField(default=True)
    producto_stock=models.IntegerField()

    def __str__(self):
        return self.producto_nombre
    
