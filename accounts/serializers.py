from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class UserSignUpSerializer(serializers.Serializer):
    email=serializers.EmailField()
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


class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()


    def validate_password(self,value):
        if(len(value)<8):
            print('LOG: INVALID PASSWORD')
            raise serializers.ValidationError("Password length not up to 8")
        return value

    def validate(self, attrs):
        super().validate(attrs)
        user=authenticate(username=attrs['email'],password=attrs['password'])
        if(not user):
            print('LOG: INVALID CREDENTIALS')
            raise serializers.ValidationError("Invalid login credentials")

        print('LOG: AUTH SUCCESS')
        
        token,_=Token.objects.get_or_create(user=user)
        attrs['token']=token
        return attrs

