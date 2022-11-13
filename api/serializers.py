from rest_framework import serializers
from .models import CaptureFrame
class CaptureFrameSerializer(serializers.Serializer):
    image=serializers.CharField(source='image.url')
    created_at=serializers.DateTimeField()

    class Meta:
        model=CaptureFrame
        fields=['image','created_at']


class UserSignUpSerializer(serializers.Serializer):
    email=serializers.EmailField()
    username=serializers.CharField()
    password=serializers.CharField()
    confirm_password=serializers.CharField()

    def validate_password(self,value):
        if(len(value)<8):
            raise serializers.ValidationError("Password length not up to 8")
        return value

    def validate(self, attrs):
        super().validate(attrs)
        if(attrs['password']!=attrs['confirm_password']):
            raise serializers.ValidationError("The passwords do not match")

        return attrs

