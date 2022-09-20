
from django.urls import path

from . import views

urlpatterns = [
    #path('home', views.index, name='index'),
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('', views.item_todisplay, name='item_todisplay'),
    #path('itm_tosearch', views.itm_tosearch, name='itm_tosearch'),
    #path('cat_tosearch', views.cat_tosearch, name='cat_tosearch'),
]
