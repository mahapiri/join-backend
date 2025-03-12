from rest_framework import permissions, viewsets
from profiles.api.serializers import ProfilesSerializer
from profiles.models import Profile


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('pk')
    serializer_class = ProfilesSerializer
    # permission_classes = [permissions.IsAuthenticated]