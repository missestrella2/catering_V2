from django.urls import path
from . import views  # Importa las vistas definidas en views.py

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('chatbot/mensaje/', views.enviar_mensaje_a_rasa, name='enviar_mensaje_a_rasa'),
    path('chatbot/mensajes_guardados/', views.obtener_mensajes_guardados, name='mensajes_guardados'),
    path('chatbot/ingrediente', views.guardar_ingrediente, name='guardar_ingrediente'),
]

