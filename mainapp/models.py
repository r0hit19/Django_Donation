from django.db import models

# Create your models here.
class homepage(models.Model):
    image=models.ImageField(upload_to='mainapp/image')

class donate(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=15)
    email=models.CharField(max_length=40)
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name

