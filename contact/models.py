from django.db import models

class Info(models.Model):
    place=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=30)
    email=models.EmailField(max_length=53)

    def __str__(self):
        return self.email