from csv import unregister_dialect
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 512, blank = False, null= False)
    email= models.CharField(max_length= 512, unique = True, blank = False, null= False)
    joined_on = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default= True)

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 512, blank = False, null= False)
    started_on = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default= True)

class Newsletter(models.Model):
    id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(Category, db_index= True, on_delete= models.CASCADE)
    title= models.CharField(max_length= 512,blank = False, null= False)
    price = models.IntegerField()
    started_on = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default= True)

class Subscription(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    newsletter_id = models.ForeignKey(Newsletter, on_delete= models.CASCADE)
    started_on = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default= True)