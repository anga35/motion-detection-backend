from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser
from .models import CaptureFrame
from .serializers import CaptureFrameSerializer
from accounts.serializers import UserSignUpSerializer
from django.contrib.auth import get_user_model
# Create your views here.

User=get_user_model()

class AddCapturedFrameView(APIView):
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]
    def post(self,request):
        print(request.FILES)
        if('captured_frame' in request.FILES):
            picture=request.FILES['captured_frame']
            frame=CaptureFrame(image=picture)
            frame.save()
            return Response({'status':200},status=200)
        else:
            return Response("No picture",status=404)

class GetAllCaptures(APIView):
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        captures=CaptureFrame.objects.order_by('-created_at')
        serializer=CaptureFrameSerializer(captures,many=True)
        for data in serializer.data :
            data['created_at']=data['created_at'][:10]
        return Response({'captures':serializer.data,'status':200})
        
#