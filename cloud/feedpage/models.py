from django.db import models

# Create your models here.
class Images (models.Model):
    caption = models.CharField(max_length=20)
    user = models.CharField(max_length=12,blank=False)
    image_data = models.FileField(upload_to="images/")
