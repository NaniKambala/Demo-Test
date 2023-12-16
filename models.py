from django.db import models

# Create your models here.
class File(models.Model):
    fileid=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    filetype=models.CharField(max_length=10)
    filename=models.CharField(max_length=50)
    file=models.FileField(upload_to='uploads/%Y/%m/%d/')

class Users(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    Confirmpassword=models.CharField(max_length=20)



