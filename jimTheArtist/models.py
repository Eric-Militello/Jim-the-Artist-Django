from django.db import models

# Create your models here.

class Painting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='paintings/')

    def __str__(self):
        return self.title
