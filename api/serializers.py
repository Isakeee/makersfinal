from rest_framework import serializers
from .models import Product, Image, Order, Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    
    "Сериализатор для избранных товаров"
    
    products = serializers.DjangoModelField()
    class Meta:
        model = Favourite
        fields = ["products"]
        


class OrderSerializer(serializers.ModelSerializer):
    
    "Сериализатор для заказов"
    
    created_at = serializers.DateTimeField(read_only=True)
    user = serializers.CharField()
    class Meta:
        model = Order
        fields = ["products", "created_at", "user"]


class ImageSerializer(serializers.ModelSerializer):
    
    "Сериализатор для добавления изображений"
    
    class Meta:
        model = Image
        fields = ("photo", "product")


class ProductSerializer(serializers.ModelSerializer):
    
    "Сериализатор для товаров"
    
    seller = serializers.ReadOnlyField(source="seller.username")
    class Meta:
        model = Product
        fields = ("name", "price", "storehouse", "seller", "phone_number")

