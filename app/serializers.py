from rest_framework import serializers
from .models import BannerImage,Cosmetics, Saloon,FoodMenu,Courses

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
