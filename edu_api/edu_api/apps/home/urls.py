from django.urls import path

from home import views

urlpatterns = [
    path("banners/", views.BannerAPIView.as_view()),
]