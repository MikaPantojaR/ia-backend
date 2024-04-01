from django.db import models
from django.contrib.auth.hashers import check_password

# Crea los modelos de datos de los usuarios

class User(models.Model):
    email = models.CharField(max_length = 40)
    nombre = models.CharField(max_length = 40)
    password = models.CharField(max_length = 40)
    rol = models.CharField(max_length = 40)
    diabetes = models.BooleanField(default = False)

    #para mostrar el nombre del usuario en el admin
    def __str__(self):
        return self.nombre
    
    def authenticate(email, password):
        user = User.objects.get(email = email)
        try:
            if password == user.password:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
