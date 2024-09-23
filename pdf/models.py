from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skills = models.TextField(max_length=1000)
    work_exp = models.TextField(max_length=1000,null=True)
    about_you = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
