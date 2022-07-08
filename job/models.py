from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255, default="Title")
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField(default=" ")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')