
from django.contrib.auth.models import User
from rest_framework import serializers

from profiles.models import Profile


class ProfilesSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)
    name = serializers.CharField(read_only=True)
    initials = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=False)

    class Meta:
        model = Profile
        fields = ['email', 'name', 'initials', 'phone']