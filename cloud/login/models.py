from django.db import models

# Create your models here.
class Login (models.Model):
    username = models.CharField(max_length=12,null=False,blank=False,unique=True)
    password = models.CharField(max_length=12,null=False,blank=False)
    def __str__(self):
        return self.username

