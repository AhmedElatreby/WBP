from django.urls import path
from . import views

app_name = "navigation"

urlpatterns = [
    path('', views.home, name="home"),
    path('options/', views.options, name="options"),
]