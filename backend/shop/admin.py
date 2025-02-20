from django.contrib import admin # type: ignore
from shop.models import DigitalProduct, Order, CategoryProduct # type: ignore
from import_export.admin import ImportExportModelAdmin # type: ignore

# Register your models here.
class DigitalProductAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

class OrderAdmin(ImportExportModelAdmin):
    list_display = ('user', 'created_at', 'is_paid')
    list_filter = ('is_paid',)
    search_fields = ('user__username',) # user__username is a lookup that searches the username field of the related User model

class CategoryProductAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(DigitalProduct, DigitalProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)