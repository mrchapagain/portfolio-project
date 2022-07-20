
from django.urls import path

from . import views

urlpatterns = [
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('', views.allanalytics, name='allanalytics'),
    path('keyword_tosearch', views.keyword_tosearch, name='keyword_tosearch'),
    path('userid_tosearch', views.userid_tosearch, name='userid_tosearch'),
]
