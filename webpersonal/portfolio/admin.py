from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    # Permitira ver los campos como lectura en el dashboard
    readonly_fields = ('created_at', 'updated_at')

# Registrando la app en el admin
admin.site.register(Project, ProjectAdmin)
