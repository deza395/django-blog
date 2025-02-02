# Generated by Django 3.1.5 on 2021-01-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, verbose_name='Nombre del Autor')),
                ('surname', models.CharField(max_length=250, verbose_name='Apellido del Autor')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('estatus', models.BooleanField(default=True, verbose_name='autor activo')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': ' Autores',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, verbose_name='nombre de categoría')),
                ('status', models.BooleanField(default=True, verbose_name='categoría activada')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': ' Categorías',
            },
        ),
    ]
