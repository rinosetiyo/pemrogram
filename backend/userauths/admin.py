from django.contrib import admin # type: ignore
from .models import User, UserProfile
from import_export.admin import ImportExportModelAdmin # type: ignore

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)