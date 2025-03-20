from django.db import models

from profiles.models import Profile

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    first_name = models.CharField(max_length=75, null=True, blank=True, editable=False)
    last_name = models.CharField(max_length=75, null=True, blank=True, editable=False)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=30)
    initial = models.CharField(max_length=2, blank=True, null=True, editable=False)
    color = models.CharField(max_length=100, blank=False, null= False)

    def __str__(self):
        return self.name
    
    def split_name(self):
        name_parts = self.name.split(' ', 1)

        if len(name_parts) > 1:
            return name_parts[0], name_parts[1]
        return self.name, None
    
    def get_initial(self):
        name_parts = self.name.split(' ', 1)

        if len(name_parts) > 1:
            return f"{name_parts[0].upper()[0]}{name_parts[1][0].upper()}"
        return self.name[0][0].upper()

    
    def save(self, *args, **kwargs):
        self.first_name, self.last_name = self.split_name()
        self.initial = self.get_initial()
        super().save(*args, **kwargs)
        
