from django.db import models

# Create your models here.

class User(models.Model):
    #Modelo de tabla usuarios
    #email, password, nombre, ap_pat, biogra, 
    #fecha nacimiento, creacion y modificacion 
    
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)

    firstst_name = models.CharField(max_length = 100)        
    last_name = models.CharField(max_length = 100)
       
    bio = models.TextField(blank = True)

    birthdate = models.TextField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateField(auto_now = True)




    