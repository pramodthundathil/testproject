from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=255)
    Price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    img = models.FileField(upload_to="product_image")
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
