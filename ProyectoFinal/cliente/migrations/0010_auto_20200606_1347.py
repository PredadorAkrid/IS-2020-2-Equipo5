# Generated by Django 3.0.3 on 2020-06-06 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_auto_20200606_1318'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='direccion',
            unique_together=set(),
        ),
    ]