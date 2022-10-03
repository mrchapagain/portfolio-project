
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allportfolioss, name='allportfolioss'),
    path('<int:portfolios_id>/', views.portfoliosdetail, name='portfoliosdetail'),
    path('home', views.home, name='home'),
]
