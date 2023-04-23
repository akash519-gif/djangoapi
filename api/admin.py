from django.contrib import admin
from api.models import Company, Employee

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',) 
    # Here above it needs tuple or list that's why we give one value and put "," after it showing that next value is null.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)