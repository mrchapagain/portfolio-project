from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class AboutMe(models.Model):
    title = models.CharField(max_length=255, default="Title")
    pub_date = models.DateTimeField()
    sum= models.TextField(max_length=255, default=" ")
    image = models.ImageField(upload_to='images/')
    body = RichTextField(default=" ")

    def __str__(self):
        return self.title

    def summary(self):
        return self.sum[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class MyCv(models.Model):
    title = models.CharField(max_length=255, default="Title")
    my_cv= models.FileField(upload_to='images/')

    def __str__(self):
        return self.title