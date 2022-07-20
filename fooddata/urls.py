
from django.urls import path

from . import views

urlpatterns = [
    #path('home', views.index, name='index'),
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('', views.allfooddatas, name='allfooddatas'),
    path('itm_tosearch', views.allfooddatas, name='itm_tosearch'),
    path('cat_tosearch', views.allfooddatas, name='cat_tosearch'),
]
