from rest_framework import serializers
from .models import BannerVideo,Cosmetics, Saloon,FoodMenu,Courses

class BannerVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = BannerVideo
        fields = ['id', 'video_url']

    def get_video_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.video.url) if obj.video else None
    

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
