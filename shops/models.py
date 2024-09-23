from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# Add my models here.

class User(AbstractUser):

    # создадим класс пользователя
    
    pass

    
class Shop(models.Model):

    # создадим класс магазина

    name = models.OneToOneField(User, verbose_name='Пользователь', blank=True, null=True, on_delete=models.CASCADE) 
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)


class Category(models.Model):

    # создаим класс категории

    name = models.CharField(verbose_name='Наименование', max_length=50)
    shops = models.ManyToManyField(Shop, verbose_name='Магазины', related_name='categories', blank=True)


class Product(models.Model):

    # создаим класс продукты

    category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, verbose_name='Название')


class ProductInfo(models.Model):

    # класс информации о продуктах

    product = models.ForeignKey(Product, verbose_name='Продукт', related_name='info_product', blank=True, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, verbose_name='Магазин', related_name='info_product', blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_rrc = models.PositiveIntegerField(verbose_name='Розничная цена')


class Parameter(models.Model):

    # класс с наименованием параметров

    name = models.CharField(max_length=55, verbose_name='Наименование')


class ProductParameter(models.Model):

    # класс с дополнительной информацией о продукте

    product_info = models.ForeignKey(ProductInfo, verbose_name='Информация о продукте', related_name='product_parameters', blank=True, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, verbose_name='Параметр', related_name='product_parameters', blank=True, on_delete=models.CASCADE)
    value = models.CharField(verbose_name='Значение', max_length=120)


class Order(models.Model):
    pass


class OrderItem(models.Model):
    pass


class Contact(models.Model):
    pass