from django.db import models

class TarjetaBIP(models.Model):

    num = models.IntegerField()
    estado = models.CharField(max_length=20)
    fecha = models.DateField()
    saldo = models.BigIntegerField()
    
