from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# Add my models here.

class User(models.Model):

    # создадим класс пользователя
    
    pass

    
class Shop(models.Model):

    # create model Shop

    name = models.OneToOneField(User, verbose_name='Пользователь', blank=True, null=True, on_delete=models.CASCADE) 
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)

