from django.urls import path
from .views import PostCreateView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', 
         PostDetailView.as_view(), 
         name='detail'),
    path('create/', 
         PostCreateView.as_view(), 
         name='create'),
]