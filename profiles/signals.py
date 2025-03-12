from contacts.models import Contact, Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Profile)
def create_contact_for_profile(sender, instance, created, **kwargs):
    if created: 
        Contact.objects.create(
            user=instance,
            name=f"{instance.user.first_name} {instance.user.last_name}",
            email=instance.user.email,
            phone=instance.phone
        )