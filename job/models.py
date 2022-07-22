from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255, default="Title")
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField(default=" ")
    body2 = RichTextField(default=" ")
    

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Tweet(models.Model):
    title = models.CharField(max_length=255, default="Title")
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField(default=" ")
    body2 = RichTextField(default=" ")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Climate(models.Model):
    title = models.CharField(max_length=255, default="Title")
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField(default=" ")
    body2 = RichTextField(default=" ")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Google(models.Model):
    title = models.CharField(max_length=255, default="Title")
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/')#, height_field=128, width_field=128
    body = models.TextField(default=" ")
    body2 = RichTextField(default=" ")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Health(models.Model):
    title = models.CharField(max_length=255, default="Title")
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField(default=" ")
    body2 = RichTextField(default=" ")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Ontology(models.Model):
    title = models.CharField(max_length=255, default="Title")
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField(default=" ")
    body2 = RichTextField(default=" ")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')