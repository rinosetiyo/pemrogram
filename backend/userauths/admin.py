from django.contrib import admin
from userauths.models import User, UserProfile
from import_export.admin import ImportExportModelAdmin



# Register your models here.
class UserAdmin(ImportExportModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date')

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
