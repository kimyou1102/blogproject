from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=15)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    todo = models.CharField(max_length=50)