from django.contrib import admin
from .models import Cliente, Credor, User_Credor

# Modificação no ADMIN
class CredorAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Credor, CredorAdmin)
admin.site.register(User_Credor)