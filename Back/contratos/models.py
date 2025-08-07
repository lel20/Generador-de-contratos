from django.db import models
from django.contrib.auth.models import User
class plantillaContrato(models.Model):
     titulo=models.CharField(max_length=200)
     descripcion=models.TextField()
     contenido=models.TextField()
     categoria=models.CharField(max_length=200)
     fecha_creacion=models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.titulo
class contratoGenerado(models.Model):
     id_usuario=models.ForeignKey(User, on_delete=models.CASCADE)  
     id_plantilla=models.ForeignKey(plantillaContrato, on_delete=models.CASCADE)
     datos_completos=models.JSONField()
     texto_completo=models.TextField()
     fecha_creacion=models.DateTimeField(auto_now_add=True)
     descarga=models.BooleanField(auto_created=False) 

     def __str__(self):
          return self.texto_completo