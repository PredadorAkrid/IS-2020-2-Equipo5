# Generated by Django 3.0.3 on 2020-04-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('descripcion', models.CharField(max_length=500, null=True)),
                ('precio', models.FloatField(default=0)),
            ],
        ),
    ]
