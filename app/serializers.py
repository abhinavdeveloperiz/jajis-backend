from rest_framework import serializers
from .models import BannerVideo

class BannerVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = BannerVideo
        fields = ['id', 'video_url']

    def get_video_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.video.url) if obj.video else None
