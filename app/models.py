from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


# Create your models here.
class HomeModel(models.Model):
     full_name = models.CharField(max_length=500)
     user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
     facebook_link = models.URLField(blank=True, null=True)
     twitter_link = models.URLField(blank=True, null=True)
     whatsapp_link = models.URLField(blank=True, null=True)
     linkedin_link = models.URLField(blank=True, null=True)
     instagram_link = models.URLField(blank=True, null=True)
     github_link = models.URLField(blank=True, null=True)
     location = models.TextField()
     email = models.EmailField(max_length=500)
     phone_call = models.CharField(max_length=500)
     whatsapp_call = models.CharField(max_length=500)
     
     
     
     
     
class ContactModel(models.Model):
     full_name = models.CharField(max_length=500)
     email = models.EmailField(max_length=500)
     subject = models.CharField(max_length=500)
     message = models.TextField(max_length=500)
     
     
     
     
class AboutModel(models.Model):
     my_name = models.CharField(max_length=500)
     my_description = models.CharField(max_length=1000)
     profile_pics = ImageField(upload_to='about')
     profile_details = models.CharField(max_length=1000)
     skills_details = models.CharField(max_length=1000)
     job = models.CharField(max_length=1000)
     website = models.URLField()
     email = models.EmailField(max_length=500)
     certificate = models.CharField(max_length=1000)
     
     
class WorkModel(models.Model):
     work_company = models.CharField(max_length=500)
     work_country = models.CharField(max_length=500)
     work_position = models.CharField(max_length=500)
     work_duration = models.CharField(max_length=500)
     work_duity = models.CharField(max_length=500)
    
class EducationModel(models.Model):
     education_name = models.CharField(max_length=500)
     education_duration = models.CharField(max_length=500)
     education_field = models.CharField(max_length=500)
     education_description = models.CharField(max_length=500)
  
  
  
  
class ServiceModel(models.Model):
     service = models.CharField(max_length=500)
  
  
  
  
  
  
  
  
  
  
  
  