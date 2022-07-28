from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Climatedf(models.Model):
    df= models.FileField('uploads/%Y/%m/%d/')


class Foodinput(models.Model):
    cat_items_dict= models.JSONField(encoder=None, decoder=None)


class Massage(models.Model):
    title = models.CharField(max_length=255, default="Title")
    massage = RichTextField(default=" ")

    def __str__(self):
        return self.title
