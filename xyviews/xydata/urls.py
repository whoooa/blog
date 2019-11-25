from django.urls import path
from xyviews.xydata import views

urlpatterns = [
    path("", views.home, name="home"),  # 主页
]
