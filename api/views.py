from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser
from .models import CaptureFrame
from .serializers import CaptureFrameSerializer
# Create your views here.


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
            return Response("Success",status=200)
        else:
            return Response("No picture",status=404)

class GetAllCaptures(APIView):

    def get(self,request):
        captures=CaptureFrame.objects.order_by('-created_at')
        serializer=CaptureFrameSerializer(captures,many=True)
        return Response({'captures':serializer.data})
        
