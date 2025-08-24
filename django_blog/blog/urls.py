from django.urls import path
from . import views

urlpatterns = [
    # Existing post URLs
    path('', views.home, name='home'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Profile URLs
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    # Comment URLs (✅ required for checks)
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    path("search/", views.search_posts, name="search_posts"),
    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name="posts_by_tag"),  

    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
