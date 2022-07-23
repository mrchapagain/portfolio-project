from django.db import models
#from .classifier import Classifier

# Create your models here.

class Tweetinput(models.Model):
    title = models.CharField(max_length=255, default="Title")
    tweetid= models.JSONField(encoder=None, decoder=None)
    keyword= models.JSONField(encoder=None, decoder=None)

    def __str__(self):
        return self.title