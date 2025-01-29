from django.contrib import admin
from .models import Category, Tag, Post, Comment
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepolulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)