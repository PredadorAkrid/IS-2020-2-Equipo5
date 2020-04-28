# Generated by Django 3.0.3 on 2020-04-28 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repartidor', '0001_initial'),
        ('platillo', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoOrden',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion_estado', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'EstadosOrden',
                'db_table': 'estado_orden',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('precio_orden', models.IntegerField(default=0)),
                ('direccion_entrega_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Direccion')),
                ('id_cliente_orden', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='cliente.Cliente')),
                ('id_estado_orden', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='administrador.EstadoOrden')),
                ('id_platillo_orden', models.ManyToManyField(null=True, to='platillo.Platillo')),
                ('id_repartidor_orden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='repartidor.Repartidor')),
            ],
            options={
                'verbose_name_plural': 'Ordenes',
                'db_table': 'orden',
            },
        ),
    ]
