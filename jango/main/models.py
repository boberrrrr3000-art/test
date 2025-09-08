from django.db import models
from user.models import user

# Create your models here.
class impytADMIN(models.Model):
    title = models.CharField('сообщение')


    def __str__(self):
        return self.title
    
