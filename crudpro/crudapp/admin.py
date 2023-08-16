from django.contrib import admin
from .models import CustomerData

# Register your models here.

@admin.register(CustomerData)
class CustomerAdmin(admin.ModelAdmin):
     list_display = ["id", "name", "email"]