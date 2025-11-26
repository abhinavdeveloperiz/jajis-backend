from rest_framework import serializers
from .models import BannerImage,Cosmetics, Saloon,FoodMenu,Courses,Product, ProductVariant,Category,Cart,CartItem
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class BannerImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerImage
        fields = "__all__"
    

class SaloonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Saloon
        fields = "__all__" 

class FoodMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMenu
        fields = ['id', 'title', 'description', 'image', 'price']

class CosmeticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosmetics
        fields = ['id', 'title', 'description', 'image', 'price']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"



# -----------------------e commerse------------------------------




class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data["user"] = user
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "quantity_label",
            "mrp",
            "price",
            "stock",
            "sku",
        ]


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)
    
  
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "brand",
            "image1",
            "image2",
            "image3",
            "image4",
            "category",
            "variants",
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)
    

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "brand",
            "description",
            "image1",
            "image2",
            "image3",
            "image4",
            "category",
            "variants",
        ]

 


class CartItemSerializer(serializers.ModelSerializer):
    variant_name = serializers.CharField(source='variant.quantity_label', read_only=True)
    price = serializers.DecimalField(source='variant.price', max_digits=10, decimal_places=2, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'variant', 'variant_name', 'quantity', 'price', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price



class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'cart_total']

    def get_cart_total(self, obj):
        return sum(item.total_price for item in obj.items.all())
