from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.

class Apply(models.Model):
    user = models.ForeignKey(User,related_name='user_apply',blank = True)
    name = models.CharField(max_length = 30)
    age  = models.PositiveIntegerField()
    email = models.EmailField()
    degree = models.CharField(max_length = 20)
    college = models.CharField(max_length = 40)
    resume = models.FileField(default = 0,upload_to='resume_files')
    date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length = 20)
    company = models.CharField(max_length = 20)
    designation = models.CharField(max_length = 2)


class CityJobs(models.Model):
    city = models.CharField(max_length = 20)
    date = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length = 30)
    designation = models.CharField(max_length = 255)
    email = models.EmailField()
    address = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 35,blank = True)
