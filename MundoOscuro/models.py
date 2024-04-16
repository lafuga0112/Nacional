from django.db import models

# Create your models here.

class Perfiles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200)
    paswd = models.CharField(max_length=200)
    estad = models.CharField(max_length=200, default=0)
    token = models.CharField(max_length=200, default=0)
    
class UsuariosPanel(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    Url_Contador = models.CharField(max_length=200)
    Url_CPA = models.CharField(max_length=200)
    token = models.CharField(max_length=200, default=0)
    plantilla = models.CharField(max_length=200, default=0)
    two_step = models.CharField(max_length=200, default=0)