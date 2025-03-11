from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def split_name(self):
        name_parts = self.name.split(' ', 1)

        if len(name_parts) > 1:
            first_name, last_name = name_parts
            return first_name, last_name
        else:
            return self.name, None
        
    def save(self, *args, **kwargs):
        self.first_name, self.last_name = self.split_name()
        super().save(*args, **kwargs)
        
