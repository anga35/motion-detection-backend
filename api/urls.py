from django.urls import path
from .views import AddCapturedFrameView,GetAllCaptures

urlpatterns = [
    path('capture-frame/',AddCapturedFrameView.as_view(),name='capture-frame'),
    path('all-captures/',GetAllCaptures.as_view(),name='all-captures')
]