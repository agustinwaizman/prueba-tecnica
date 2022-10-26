from django.db import models
from datetime import date, datetime


class Palabra(models.Model):
    contenido = models.CharField(max_length=20, blank=False, null=False)
    esPalindromo = models.BooleanField(default=False)
    creacion = models.DateTimeField(default = datetime.now)
    update = models.DateTimeField(default = datetime.now)

    def __str__(self) -> str:
        return self.contenido
