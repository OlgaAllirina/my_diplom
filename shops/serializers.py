from rest_framework import serializers
from models import *


class ShopSerializer(serializers.ModelSerializer):

    # создадим сериализатор на основе модели Shop

    class Meta:
        model = Shop 
        fields = ('id', 'name', 'state',) # поля, которые будут видны
        realy_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):

    # создадим сериализатор на основе модели User
    
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email', 'company', 'position', 'contacts','avatar')
        read_only_fields = ('id',) # поля, которые будут видны


class CategorySerializer(serializers.ModelSerializer):

    # создадим сериализатор на основе модели Contact
     
    class Meta:
        model = Category
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    
    # создадим сериализатор на основе модели Product

    class Meta:
        model = Product
        fields = ('name', 'category',)


class ContactSerializer(serializers.ModelSerializer):

    # создадим сериализатор на основе модели Contact

    class Meta:
        model = Contact
        fields = ('id', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'user', 'phone')
        read_only_fields = ('id',)
        extra_kwargs = {
            'user': {'write_only': True}
        }

class ProductParameterSerializer(serializers.ModelSerializer):

# создадим сериализатор на основе модели ProductParameter

    class Meta:
        model = ProductParameter
        fields = ('parameter', 'value',)