# Generated by Django 3.0.3 on 2020-04-09 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id_repatidor', models.AutoField(db_column='id_repatidor', primary_key=True, serialize=False)),
                ('nombre_repartidor', models.CharField(max_length=64)),
                ('apellido_paterno_repartidor', models.CharField(max_length=100)),
                ('apellido_materno_repartidor', models.CharField(max_length=100)),
                ('correo_repartidor', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Repartidores',
                'db_table': 'repartidor',
            },
        ),
    ]