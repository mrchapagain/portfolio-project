from django.db import models
#from .classifier import Classifier

# Create your models here.

class Tweetid(models.Model):
    tweetid= models.JSONField(encoder=None, decoder=None, null=True)

    #def __str__(self):
        #return self.name

class Tweetkeyword(models.Model):
    keyword= models.JSONField(encoder=None, decoder=None, null=True)

    #def __str__(self):
        #return self.name
        