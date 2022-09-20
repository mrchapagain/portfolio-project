from django.db import models
from ckeditor.fields import RichTextField

# Class for dataset
class Dataset(models.Model):
    df= models.FileField('uploads/%Y/%m/%d/')
    
    def __str__(self):
        return self.title


# Class for food category for user input
class Category(models.Model):
    food_category_dict= models.JSONField(encoder=None, decoder=None)

    def __str__(self):
        return self.title

    