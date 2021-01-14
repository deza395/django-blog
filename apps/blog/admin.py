from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin( ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['name'] 
    list_display=('name','status', 'creation_date',)
    resource_class = CategoryResource



class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name','surname', 'email'] 
    list_display=('name','surname','estatus', 'creation_date')
    resource_class = AuthorResource


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin( ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['name'] 
    list_display=('title','slug','description','content','image','author','category', 'status', 'creation_date')
    resource_class = PostResource


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)

