from rest_framework import viewsets
from contacts.api.serializers import ContactsSerializer
from contacts.models import Contact

# Create your views here.
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactsSerializer