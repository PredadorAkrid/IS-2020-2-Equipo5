# Generated by Django 3.0.3 on 2020-04-08 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repartidor', '0002_auto_20200408_1202'),
        ('administrador', '0003_auto_20200408_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='id_repartidor_orden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='repartidor.Repartidor'),
        ),
    ]
