from rest_framework import serializers
from models import Shop


class ShopSerializer(serializers.ModelSerializer):
    # создадим сериализатор на основе модели Shop
    class Meta:
        model = Shop 
        fields = ('id', 'name',) # поля, которые будут видны