# Generated by Django 4.2.17 on 2024-12-20 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculos', '0004_remove_catering_receta_catering_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='recetaingrediente',
            name='cantidad_necesaria',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
