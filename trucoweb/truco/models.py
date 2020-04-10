from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=200)
    ranking = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

