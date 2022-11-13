from django.db import models

# Create your models here.

def upload_capture(instance,filename):
    return f'frame_capture/{filename}'


class CaptureFrame(models.Model):
    image=models.ImageField(upload_to=upload_capture)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "CapturedFrame"