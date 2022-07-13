
from django.urls import path

from . import views

urlpatterns = [
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('', views.allanalytics, name='allanalytics'),
    path('home', views.index, name='index'),
    path('crawl', views.result, name='result'),
]
