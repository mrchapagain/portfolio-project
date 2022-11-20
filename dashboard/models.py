from django.db import models
from ckeditor.fields import RichTextField
#from separatedvaluesfield.models import SeparatedValuesField

# Class for dataset
class Dataset(models.Model):
    df= models.FileField('uploads/%Y/%m/%d/')
    
    #def __str__(self):
        #return self.title


# Class for food category for user input
class Category(models.Model):
    food_category_dict= models.JSONField(encoder=None, decoder=None)

    def __str__(self):
        return self.title

# Class for Flavour Network arguments
#class Flavour(models.Model):
    #title = models.CharField(max_length=255, default=" ")
    #flavour_foodname = SeparatedValuesField(max_length=1350, token=',')

    #def __str__(self):
        #return self.title

    