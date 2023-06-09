from django.db import models

class Sensores(models.Model):
    temperatura = models.FloatField()
    peso = models.FloatField()
    humedad = models.IntegerField()

class Lecturas(models.Model):
    key = models.TextField()
    value = models.FloatField()
    date_created = models.DateTimeField()

