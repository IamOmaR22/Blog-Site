from django.db import models

class login(models.Model):
    email=models.EmailField(max_length=120)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email

