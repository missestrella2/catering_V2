from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Receta, RecetaIngrediente, Ingrediente, Catering
from .forms import IngredienteForm, RecetaForm, CateringForm, RecetaIngredienteForm

# Vista para calcular el catering
def calcular_catering(request):
    if request.method == 'POST':
        catering_form = CateringForm(request.POST)
        if catering_form.is_valid():
            catering = catering_form.save()
            receta = catering.receta
            cantidad_personas = catering.cantidad_personas

            ingredientes_receta = RecetaIngrediente.objects.filter(receta=receta)
            lista_compras = []
            for item in ingredientes_receta:
                cantidad_total = item.cantidad_necesaria * cantidad_personas
                lista_compras.append({
                    'ingrediente': item.ingrediente.nombre,
                    'cantidad': cantidad_total,
                    'unidad': item.ingrediente.unidad
                })

            return render(request, 'calculos/resultado.html', {
                'receta': receta,
                'cantidad_personas': cantidad_personas,
                'lista_compras': lista_compras
            })
    else:
        catering_form = CateringForm()

    return render(request, 'calculos/calcular.html', {'catering_form': catering_form})

# Vista para el home principal
def home(request):
    return render(request, 'home.html')

# Vista para el home de calculos
def home_calculos(request):
    return render(request, 'calculos/home_calculos.html')

# Gestionar ingredientes
def agregar_ingrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ingredientes')
    else:
        form = IngredienteForm()
    return render(request, 'calculos/agregar_ingrediente.html', {'form': form})

def lista_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'calculos/lista_ingredientes.html', {'ingredientes': ingredientes})

# Gestionar recetas
def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            receta = form.save()
            return redirect('editar_receta', pk=receta.pk)
    else:
        form = RecetaForm()
    return render(request, 'calculos/agregar_receta.html', {'form': form})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'calculos/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    ingredientes = RecetaIngrediente.objects.filter(receta=receta)
    return render(request, 'calculos/detalle_receta.html', {'receta': receta, 'ingredientes': ingredientes})

def editar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    ingredientes = RecetaIngrediente.objects.filter(receta=receta)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'calculos/editar_receta.html', {'form': form, 'receta': receta, 'ingredientes': ingredientes})

def eliminar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        receta.delete()
        return redirect('lista_recetas')
    return render(request, 'calculos/eliminar_receta.html', {'receta': receta})

# Gestionar ingredientes en recetas
def agregar_receta_ingrediente(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        form = RecetaIngredienteForm(request.POST)
        if form.is_valid():
            ingrediente_receta = form.save(commit=False)
            ingrediente_receta.receta = receta
            ingrediente_receta.save()
            return redirect('editar_receta', pk=receta.pk)
    else:
        form = RecetaIngredienteForm()
    return render(request, 'calculos/agregar_receta_ingrediente.html', {'form': form, 'receta': receta})

def eliminar_ingrediente_receta(request, pk):
    ingrediente_receta = get_object_or_404(RecetaIngrediente, pk=pk)
    receta_id = ingrediente_receta.receta.pk
    if request.method == 'POST':
        ingrediente_receta.delete()
        return redirect('editar_receta', pk=receta_id)
    return render(request, 'calculos/eliminar_ingrediente.html', {'ingrediente_receta': ingrediente_receta})

# Gestionar catering
def agregar_catering(request):
    if request.method == 'POST':
        form = CateringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_caterings')
    else:
        form = CateringForm()
    return render(request, 'calculos/agregar_catering.html', {'form': form})

def lista_caterings(request):
    caterings = Catering.objects.all()
    return render(request, 'calculos/lista_caterings.html', {'caterings': caterings})

# AJAX para agregar ingredientes a recetas
def agregar_ingrediente_ajax(request):
    if request.method == 'POST':
        form = RecetaIngredienteForm(request.POST)
        if form.is_valid():
            ingrediente_receta = form.save()
            receta = ingrediente_receta.receta
            ingredientes = RecetaIngrediente.objects.filter(receta=receta)
            html = render_to_string('calculos/ingredientes_lista.html', {'ingredientes': ingredientes})
            return JsonResponse({'html': html})
    return JsonResponse({'error': 'Formulario inválido'}, status=400)
