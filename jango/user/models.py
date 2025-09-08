from django.db import models

# Create your models here.
class user(models.Model):
    login = models.CharField('Логин')
    password = models.CharField('Пороль')

    def __str__(self):
        return self.login

