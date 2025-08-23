from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.posts, name="posts"),  # ✅ add this
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
]
