# Generated by Django 3.0.3 on 2020-06-06 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0012_auto_20200606_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_cliente',
            field=models.AutoField(db_column='id_cliente', primary_key=True, serialize=False),
        ),
    ]