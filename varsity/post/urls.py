from django.urls import path, include
from post.cbv import ListCreateCompanyAPIView, CompanyAPIView, ListCreatePostAPIView, PostAPIView

urlpatterns = [
    path('companies/', ListCreateCompanyAPIView.as_view()),
    path('companies/<int:pk>/', CompanyAPIView.as_view()),
    path('posts/', ListCreatePostAPIView.as_view()),
    path('posts/<int:pk>/', PostAPIView.as_view()),
]