
from django.urls import path

from . import views

urlpatterns = [
    path('', views.alldocs, name='alldocs'),
    path('<int:aboutme_id>/', views.docdetail, name='docdetail'),

]
