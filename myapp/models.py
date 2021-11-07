from django.db import models

# Create your models here.
class Blog(models.Model):
    heading =models.CharField(max_length=150)
    desc =models.CharField(max_length=20000)
    date= models.DateField()