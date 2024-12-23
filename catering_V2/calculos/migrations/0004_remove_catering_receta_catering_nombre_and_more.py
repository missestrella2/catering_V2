# Generated by Django 4.2.17 on 2024-12-20 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculos', '0003_receta_porciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catering',
            name='receta',
        ),
        migrations.AddField(
            model_name='catering',
            name='nombre',
            field=models.CharField(default='Catering genérico', max_length=100),
        ),
        migrations.AlterField(
            model_name='catering',
            name='cantidad_personas',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='CateringReceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porciones', models.PositiveIntegerField()),
                ('catering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to='calculos.catering')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculos.receta')),
            ],
        ),
    ]
