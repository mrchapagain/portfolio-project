from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Googledf(models.Model):
    df= models.FileField('uploads/%Y/%m/%d/')


class Country_Name(models.Model):
    pn= models.JSONField(encoder=None, decoder=None)
    #def __str__(self):
       # return self.name


class Massage(models.Model):
    title = models.CharField(max_length=255, default="Title")
    massage = RichTextField(default=" ")

    def __str__(self):
        return self.title

class Trendskeyword(models.Model):
    keyword= models.JSONField(encoder=None, decoder=None, null=True)

    #def __str__(self):
       # return self.name

class Category(models.Model):
    cat= models.JSONField(encoder=None, decoder=None, null=True)


class TimeFrame(models.Model):
    time= models.JSONField(encoder=None, decoder=None, null=True)

class SearchType(models.Model):
    type= models.JSONField(encoder=None, decoder=None, null=True)

