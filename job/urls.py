
from django.urls import path

from . import views

urlpatterns = [
    path('', views.alljobs, name='alljobs'),
    #path('<int:blog_id>/', views.detail, name='detail'),
]
