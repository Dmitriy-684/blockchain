
from django.contrib import admin
from django.urls import path
from mainTatarin import views

urlpatterns = [
    path("", views.home_page),
    path("admin/", admin.site.urls),
    path("login/", views.user_authorization),
    path("post-wallet/", views.post_for_authorization),
    path("get-theory/", views.get_theory),
    path("get-character/", views.get_character),
    path("post-character/", views.post_for_character),
    path("register/", views.user_registration),
    path("post-user/", views.post_for_registration),
    path("get-level/", views.get_level),
    path("post-level/", views.post_for_level),
    path("check-answer/", views.check_answer),
]

