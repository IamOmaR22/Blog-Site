from django.db import models

class about(models.Model):
    name=models.TextField(max_length=120)
    designation=models.TextField(max_length=100 , null=True)
    department=models.TextField(max_length=100, null=True)
    university=models.TextField(max_length=100, null=True)
    email=models.EmailField(max_length=100, null=True)
    cell=models.TextField(max_length=100, null=True)
    image=models.ImageField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return self.name

