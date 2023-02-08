from django.urls import path
from .views import *

urlpatterns = [
    path('api/upload/image', UploadView.as_view(), name = 'face_detection'),
]