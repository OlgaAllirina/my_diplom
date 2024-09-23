from rest_framework import serializers
from models import Shop, User


class ShopSerializer(serializers.ModelSerializer):
    # создадим сериализатор на основе модели Shop
    class Meta:
        model = Shop 
        fields = ('id', 'name',) # поля, которые будут видны


class UserSerializer(serializers.ModelSerializer):
    # создадим сериализатор на основе модели Shop
    class Meta:
        model = User 
        fields = ('id', 'name',) # поля, которые будут видны