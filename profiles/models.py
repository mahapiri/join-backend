from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=False, null=False)

    @property
    def name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    @property
    def email(self):
        return self.user.email

    @property
    def initials(self):
        first_name = self.user.first_name.strip() if self.user.first_name else ""
        last_name = self.user.last_name.strip() if self.user.last_name else ""

        if first_name and last_name:
            return f"{first_name[0]}{last_name[0]}"
        elif first_name:
            return first_name[0]
        elif last_name:
            return last_name[0]
        return "N/A"  # Falls kein Name vorhanden ist

    def __str__(self):
        return f"Profile of {self.user.username}"
