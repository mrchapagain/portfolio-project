
from django.urls import path

from . import views

urlpatterns = [
    path('', views.alldocs, name='alldocs'),
    path('<int:doc_id>/', views.docdetail, name='docdetail'),
]
