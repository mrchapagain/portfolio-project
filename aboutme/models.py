from django.db import models

# Create your models here.
class AboutMe(models.Model):
    title = models.CharField(max_length=255)
    #image = models.ImageField(upload_to='images/')
    #summary = models.CharField(max_length=500)
    #file = models.FileField(upload_to='static/', max_length=100)

    def __str__(self):
        return self.title
