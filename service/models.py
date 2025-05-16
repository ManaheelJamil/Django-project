from django.db import models

class Service(models.Model):
    service_icon= models.CharField(max_length=50)
    service_title= models.CharField(max_length=50)
    service_des=models.TextField()

class About(models.Model):
    about_icon= models.CharField(max_length=50)
    about_title= models.CharField(max_length=50)
    about_des=models.TextField()

class Contact(models.Model):
    contact_text= models.CharField(max_length=50)