# Generated by Django 4.2.17 on 2024-12-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculos', '0002_remove_receta_ingredientes_ingrediente_unidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='porciones',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
