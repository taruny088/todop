from django.db import models

# Create your models here.
class Regmodel(models.Model):
    username=models.CharField(max_length=20)
    task_name=models.CharField(max_length=100)
    disc=models.CharField(max_length=150)
    pic=models.ImageField(upload_to='pic/')

    def __str__(self):
        return self.username