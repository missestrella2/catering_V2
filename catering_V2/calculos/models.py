from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.FloatField()  # Cantidad en la unidad del ingrediente
    unidad = models.CharField(max_length=100, default='default_unit')
    #unidad = models.CharField(max_length=50)  # Ejemplo: gramos, litros, unidades
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio total

    def __str__(self):
        return f"{self.nombre} ({self.marca}) - {self.cantidad}{self.unidad}"


class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    porciones = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.nombre} ({self.porciones} porciones)"



# Tabla intermedia para definir ingredientes en recetas
class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad_necesaria = models.FloatField()  # Cantidad necesaria para esta receta
    unidad = models.CharField(max_length=50)  # Unidad específica

    def __str__(self):
        return f"{self.cantidad_necesaria}{self.unidad} de {self.ingrediente} para {self.receta}"


class Catering(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    cantidad_personas = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad_personas} personas para {self.receta}"



