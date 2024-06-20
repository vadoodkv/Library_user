from django.db import models

# Create your models here.



class addin(models.Model):
    Book_id=models.IntegerField()
    Book_name=models.CharField(max_length=250)
    Borr_id=models.IntegerField()
    Name=models.CharField(max_length=250)
    Address=models.CharField(max_length=250)
    Phone=models.IntegerField()
    
    
    
    
    
    