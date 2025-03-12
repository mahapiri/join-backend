from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, null=False, blank= False)
    email = models.EmailField(max_length=155, null=False, blank=False)
    phone = models.CharField(max_length=30, blank=False, null=False)
    
    @property
    def name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    @property
    def initials(self):
        return f"{self.user.first_name[0]}{self.user.last_name[0]}"
    
    def __str__(self):
        return f"Profile of {self.user.username}"
    

