from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSignUpSerializer,LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

User=get_user_model()
# Create your views here.
class CreateUserView(APIView):
    def post(self,request):

        data=request.data.dict()
        serializer=UserSignUpSerializer(data=data)
        is_valid=serializer.is_valid()
        if(not is_valid):
            return Response(serializer.errors)
        del data['confirm_password']

        User.objects.create_user(**data)
        return Response({'status':200},status=200)

class LoginView(APIView):
    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        is_valid=serializer.is_valid()
        if(not is_valid):
            return Response(serializer.errors,status=400)

        return Response({'access_token':serializer.validated_data['token'].key})