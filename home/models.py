from django.db import models

# Create your models here.
from django.db import models


class photo(models.Model):
    location=models.TextField(max_length=100)
    date=models.DateField()
    image = models.ImageField(upload_to='photography/', blank=True)

    def __str__(self):
        return self.location

class myquote(models.Model):
    title = models.TextField(max_length=100)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

