from django.db import models

# Create your models here.
class chat(models.Model):
    text=models.TextField(max_length=300)
    name = models.TextField(max_length=50, null=True)
    def __str__(self):
        return self.text