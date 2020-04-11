import platillo.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('descripcion', models.CharField(max_length=500, null=True)),
                ('precio', models.FloatField(default=0)),
                ('imagen', models.ImageField(null=True,
                                             upload_to=platillo.models.directorio_imagen)),
                ('categoria', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='categoria.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Platillos',
                'db_table': 'platillo',
            },
        ),
    ]
