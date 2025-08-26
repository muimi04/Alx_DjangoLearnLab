from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path, include  
import posts.views as views


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path('feed/', views.feed, name='feed'),
]