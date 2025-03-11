
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from profiles.api.serializers import ProfilesSerializer


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = ProfilesSerializer
    # permission_classes = [permissions.IsAuthenticated]