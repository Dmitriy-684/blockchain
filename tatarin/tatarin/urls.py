
from django.contrib import admin
from django.urls import path
from mainTatarin import views

urlpatterns = [
    path("", views.home_page),
    path("admin/", admin.site.urls),
    path("login/", views.user_authorization),
    path("post-wallet/", views.post_for_authorization),
]

