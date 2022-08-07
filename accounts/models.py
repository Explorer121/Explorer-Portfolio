from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProfileModel(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     # auth_token = models.CharField(max_length=255)
     image = models.ImageField(upload_to='profile')
     created_at = models.DateTimeField(auto_now_add=True)
     is_verified = models.BooleanField(default=False)
     
     
     def __str__(self):
          return self.user.username
     