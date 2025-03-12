from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from contacts.api.serializers import ContactsSerializer
from contacts.models import Contact

# Create your views here.
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactsSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ContactDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all().order_by('pk')
    serializer_class = ContactsSerializer
    permission_classes = [AllowAny]