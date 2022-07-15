
from django.urls import path

from . import views

urlpatterns = [
    path('', views.alljobs, name='alljobs'),
    path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
]
