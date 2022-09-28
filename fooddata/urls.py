
from django.urls import path

from . import views

urlpatterns = [
    #path('home', views.index, name='index'),
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('', views.allfooddatas, name='allfooddatas'),
    path('keyword_tosearch', views.keyword_tosearch, name='keyword_tosearch'),
    path('timeframe_tosearch', views.timeframe_tosearch, name='timeframe_tosearch'),
]
