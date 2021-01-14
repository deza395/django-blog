from django.db import models
from ckeditor.fields  import RichTextField

# Create your models here.

class Category (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('nombre de categoría', max_length=250, null=False, blank=False)
    status = models.BooleanField ('categoría activada', default = True)
    creation_date = models.DateField('fecha de creacion', auto_now_add= True )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = ' Categorías'

    def __str__(self):
        return self.name

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre del Autor', max_length=250, null= False, blank= False)
    surname = models.CharField('Apellido del Autor', max_length=250, null= False, blank= False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    email = models.EmailField('Correo electrónico', null=False, blank=False)
    estatus = models.BooleanField('autor activo', default=True)
    creation_date = models.DateField('fecha de creacion', auto_now_add= True )
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = ' Autores'
    
    def __str__(self):
            return "{0},{1}".format(self.name,self.surname)



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=250, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    description = models.CharField('Descripción', max_length=250, null=False, blank = False)
    content = RichTextField('contenido')
    image = models.URLField(max_length=2500, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    status = models.BooleanField('Publicado', default= True)
    creation_date = models.DateField('Fecha de publicación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
            return self.title



