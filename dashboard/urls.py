
from django.urls import path

from . import views

urlpatterns = [
    #path('home', views.index, name='index'),
    #path('<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('', views.item_todisplay, name='item_todisplay'),
    path('Food_category', views.Food_category, name='Food_category'),
    path('foodname_todf', views.foodname_todf, name='foodname_todf'),
]