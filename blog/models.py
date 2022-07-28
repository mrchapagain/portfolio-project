from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    sum = models.TextField(max_length=255, default=" ")
    image = models.ImageField(upload_to='images/')
    body = RichTextField(default=" ")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.sum[:500]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')