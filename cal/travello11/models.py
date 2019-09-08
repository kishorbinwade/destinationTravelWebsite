
from django.db import models

# Create your models here.
class destination(models.Model):
    """
    id: int    #django take automatic ID so we dont have to declare
    name: str #for data base connnectivity and migration we use different syntax
    img:str
    desc:str
    price:int 
    offer:bool
    #pics is a folder for image"""  
    
  
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics') 
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)