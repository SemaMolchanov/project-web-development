from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from webproj_api.class_views import GameListAPIView, GameDetailAPIView

# Create your models here.

urlpatterns=[
    path('login/', obtain_jwt_token),
    path('games/', GameListAPIView.as_view()),
    path('games/<int:pk>/', GameDetailAPIView.as_view()),
]