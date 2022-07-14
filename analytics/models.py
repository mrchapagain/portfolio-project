from django.db import models
#from .classifier import Classifier

# Create your models here.
from django.db import models
from django_matplotlib import MatplotlibFigureField

class MyModel(models.Model):
    figure = MatplotlibFigureField(figure='my_figure')