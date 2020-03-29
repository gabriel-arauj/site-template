from django.urls import path, include
from backend.home import views
urlpatterns = [
    path('', views.index, name='index'),
]
