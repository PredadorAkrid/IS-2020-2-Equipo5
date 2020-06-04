# Generated by Django 3.0.3 on 2020-06-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20200604_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='id_platillo_carrito',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='carrito',
            unique_together={('id_platillo_carrito', 'id_cliente_carrito')},
        ),
    ]
