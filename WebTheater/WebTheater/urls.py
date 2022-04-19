

from django.urls import path
from WebTheater import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<id>/', views.video, name='videos')
]
