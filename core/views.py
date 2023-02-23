from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductosSerializer
from .models import Productos

# Create your views here.


class ProductosList(generics.ListAPIView):
    #SELECT * FROM PRODUCTOS
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    

class ProductosCreate(generics.CreateAPIView):
    #SELECT * FROM PRODUCTOS
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer    
