from django.contrib import admin
from .models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_editable = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'department')
    list_display = ('id', 'first_name', 'last_name', 'department')
    list_filter = ('first_name', 'last_name', 'department')
    search_fields = ('first_name', 'last_name', 'department')
    list_editable = ('first_name', 'last_name')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
