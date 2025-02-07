from django.contrib import admin # type: ignore
from blog.models import Post, Comment
from import_export.admin import ImportExportModelAdmin # type: ignore

# Register your models here.
class PostAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)