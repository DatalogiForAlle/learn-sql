from django.contrib import admin

from .models import Customer, City


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'age', 'city')


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'size')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(City, CityAdmin)
