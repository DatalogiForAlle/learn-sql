from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'customer_name', 'contact_last_name', 'contact_first_name')


admin.site.register(Customer, CustomerAdmin)
