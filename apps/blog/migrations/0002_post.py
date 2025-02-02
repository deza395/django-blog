# Generated by Django 3.1.5 on 2021-01-13 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('description', models.CharField(max_length=250, verbose_name='Descripción')),
                ('content', models.TextField(default='agregue contenido', verbose_name='contenido')),
                ('image', models.URLField(max_length=2500)),
                ('status', models.BooleanField(default=True, verbose_name='Publicado')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de publicación')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
