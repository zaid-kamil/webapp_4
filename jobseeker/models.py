from django.db import models

# Create your models here.
class Person(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    cover_letter = models.FileField(upload_to='cover_letter/', blank=True, null=True)
    education = models.CharField("Highest Education ", max_length=15 ,blank=True, null=True)
    mark_hs = models.CharField("HighSchool Marks",max_length=10, blank=True, null=True)
    mark_grad = models.CharField("Graduation Marks",max_length=10, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
