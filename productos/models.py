from django.db import models

class  Chela(models.Model):
    marca = models.CharField(max_length = 50)
    #4 valores digitos y 2 decimales
    alcohol = models.DecimalField(max_digits = 4, decimal_places= 2 )
    militros = models.IntegerField()
    artesanal = models.BooleanField()
    nacionalidad = models.CharField(max_length=50, blank=True, null = True)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
    
    ##nos sirve para saber como va a mostrar los registros en el panel
    def __str__(self):
        return self.marca

