
from django.urls import path

from . import views

urlpatterns = [
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('', views.allanalytics, name='allanalytics'),
    path('home', views.index, name='index'),
    path('keywordsearch', views.keywordsearch, name='keywordsearch'),
]
