from django.urls import path
from .views import ProductosList,ProductosCreate

#Endpoint
urlpatterns = [
    path('api/productsall/', ProductosList.as_view()),
    path('api/productoscreate/', ProductosCreate.as_view()),

]    