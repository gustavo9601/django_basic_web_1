from django.db import models


# Create your models here.
class Project(models.Model):
    # verbose_name // nombre en el dashboard
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.CharField(max_length=500, verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to="projects")  # se especifica en que carpeta debe subir
    link = models.URLField(null=True, blank=True, verbose_name='Direccion web') # Es nullo y puede ser vacio
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')  # Se ejecuta al crearce el registro
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizacion')  # se ejecuta cada actualizacion

    # Configuracion para el dashboard admin
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created_at'] # -created_at ordena de forma descendente

    # devolvera en la tabla de proyectos
    def __str__(self):
        return self.title