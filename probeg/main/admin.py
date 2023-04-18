from django.contrib import admin

from .models import *


class AdminRunner(admin.ModelAdmin):
    list_display = [field.name for field in DjRunner._meta.fields]


class AdminResult(admin.ModelAdmin):
    list_display = [field.name for field in DjResult._meta.fields]


admin.site.register(DjRunner, AdminRunner)
admin.site.register(DjResult, AdminResult)
admin.site.register(DjCountry)
admin.site.register(DjCategorySize)
