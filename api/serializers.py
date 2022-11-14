from rest_framework import serializers
from .models import CaptureFrame
class CaptureFrameSerializer(serializers.Serializer):
    image=serializers.CharField(source='image.url')
    created_at=serializers.DateTimeField()

    class Meta:
        model=CaptureFrame
        fields=['image','created_at']
