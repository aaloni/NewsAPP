from django.contrib.auth.models import AbstractUser
from django.db import models


#Create user table
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    national_id = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True,blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.national_id

#Create article table
class Article(models.Model):
    pub_date = models.DateField(null=True,blank=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(null=True,blank=True,)
    url=models.URLField(null=True,blank=True,)
    publishedat = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
