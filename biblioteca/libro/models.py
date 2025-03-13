from django.db import models

# Create your models here.
""" creacionn de la tbala Autor, para la base de datos """


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    """ max_length -> numero maximo de caracteres """
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    """ Para descripciones o cajas de texto """
    descripcion = models.TextField(blank=False,null=False)
