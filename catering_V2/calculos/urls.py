from django.urls import path
from . import views

urlpatterns = [
    path('calcular/', views.calcular_catering, name='calcular_catering'),
    path('calculos/', views.home_calculos, name='home_calculos'),  # Nueva ruta
    path('agregar/ingrediente/', views.agregar_ingrediente, name='agregar_ingrediente'),
    path('agregar/receta/', views.agregar_receta, name='agregar_receta'),
    path('recetas/<int:pk>/ingredientes/agregar/', views.agregar_receta_ingrediente, name='agregar_ingrediente_receta'),
    path('agregar/catering/', views.agregar_catering, name='agregar_catering'),
    path('caterings/', views.lista_caterings, name='lista_caterings'),
    path('agregar/ingrediente/', views.agregar_ingrediente, name='agregar_ingrediente'),
    path('ingredientes/', views.lista_ingredientes, name='lista_ingredientes'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('recetas/<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('recetas/<int:pk>/editar/', views.editar_receta, name='editar_receta'),
    path('recetas/<int:pk>/eliminar/', views.eliminar_receta, name='eliminar_receta'),
    path('recetas/ingredientes/<int:pk>/eliminar/', views.eliminar_ingrediente_receta, name='eliminar_ingrediente_receta'),
    path('recetas/ingredientes/<int:pk>/editar/', views.editar_ingrediente_receta, name='editar_ingrediente_receta'),
]

