from django.contrib import admin
from .models import Clients

# Register your models here
class AdminClients(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "age",
        "published",
    )
    
    list_display_links = (
        "name",
        "surname",
    )
    
    list_editable = (
        "published",
    )
    
admin.site.register(Clients, AdminClients)
