
from django.urls import path

from . import views

urlpatterns = [
    #path('home', views.index, name='index'),
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('', views.allfooddatas, name='allfooddatas'),
]
