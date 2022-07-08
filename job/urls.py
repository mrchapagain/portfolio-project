
from django.urls import path

from . import views

urlpatterns = [
    path('', views.alljobs, name='alljobs'),
    path('<int:job_id>/', views.jobdetail, name='jobdetail'),
]
