from django.db import models

# Create your models here.
class Climatedf(models.Model):
    title = models.CharField(max_length=255, default="Title")
    df= models.FileField('uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title