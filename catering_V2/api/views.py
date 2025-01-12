import requests
import json
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
from calculos.models import Ingrediente

# Renderiza la página del chatbot
def chatbot_view(request):
    return render(request, 'api/chatbot.html')

# Enviar mensaje a Rasa y guardar en la base de datos
@csrf_exempt
def enviar_mensaje_a_rasa(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            user_message = body.get("message")

            if not user_message:
                return JsonResponse({"error": "No se recibió ningún mensaje"}, status=400)

            # Guardar mensaje del usuario en la base de datos
            ChatMessage.objects.create(sender="user", message=user_message)

            # Enviar mensaje al servidor de Rasa
            rasa_response = requests.post(
                "https://localhost:5005/webhooks/rest/webhook",
                json={"sender": "user", "message": user_message},
            )

            if rasa_response.status_code == 200:
                responses = rasa_response.json()
                bot_responses = []

                for response in responses:
                    if "text" in response:
                        bot_responses.append({"text": response["text"]})
                        # Guardar respuesta del bot en la base de datos
                        ChatMessage.objects.create(sender="bot", message=response["text"])

                return JsonResponse(bot_responses, safe=False, status=200)

            return JsonResponse({"error": "Error al conectar con Rasa"}, status=500)

        except Exception as e:
            return JsonResponse({"error": f"Error inesperado: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)

# Obtener mensajes guardados en la base de datos
def obtener_mensajes_guardados(request):
    if request.method == "GET":
        mensajes = ChatMessage.objects.order_by('-timestamp')
        datos = [
            {
                "sender": mensaje.sender,
                "message": mensaje.message,
                "timestamp": mensaje.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
            for mensaje in mensajes
        ]
        return JsonResponse(datos, safe=False)

    return JsonResponse({"error": "Método no permitido"}, status=405)

# Crear un ingrediente en la base de datos

# views.py (api)
# views.py (api)
import json
from decimal import Decimal
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from calculos.models import Ingrediente

@csrf_exempt
def guardar_ingrediente(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        # Extrae los datos del JSON
        nombre = data.get("ingrediente")  # O "nombre" si cambiaste la key
        marca = data.get("marca")
        cantidad = data.get("cantidad")
        unidad = data.get("unidad")
        precio = data.get("precio")

        # Haz validaciones básicas (por ejemplo, que no vengan nulos si son obligatorios)
        if not nombre or not cantidad or not precio:
            return JsonResponse({"error": "Faltan datos obligatorios"}, status=400)

        try:
            # Convertir a Decimal
            cantidad_decimal = Decimal(str(cantidad).replace(",", "."))
            precio_decimal   = Decimal(str(precio).replace(",", "."))

            # Crear el objeto en la BD
            ingrediente_obj = Ingrediente.objects.create(
                nombre=nombre,
                marca=marca,
                cantidad=cantidad_decimal,
                unidad=unidad if unidad else "gramos",  # o lo que quieras por default
                precio=precio_decimal
            )

            return JsonResponse({
                "message": "Ingrediente guardado con éxito",
                "id": ingrediente_obj.id  # si quieres devolver el id creado
            }, status=201)

        except Exception as e:
            return JsonResponse({
                "error": f"Ocurrió un error al guardar el ingrediente: {str(e)}"
            }, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)
