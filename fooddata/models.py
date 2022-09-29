from django.db import models
from ckeditor.fields import RichTextField

class Country_Name(models.Model):
    pn= models.JSONField(encoder=None, decoder=None)
    #def __str__(self):
       # return self.name

class Trendskeyword(models.Model):
    keyword= models.JSONField(encoder=None, decoder=None, null=True)

    #def __str__(self):
       # return self.name

class TimeFrame(models.Model):
    time= models.JSONField(encoder=None, decoder=None, null=True)
