
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allanalytics, name='allanalytics'),
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
]
