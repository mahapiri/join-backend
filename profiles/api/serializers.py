
from django.contrib.auth.models import User
from rest_framework import serializers

from profiles.models import Profile


class ProfilesSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(source='user.email')
    name = serializers.CharField(read_only=True)
    initials = serializers.CharField(read_only=True)
    phone = serializers.CharField(max_length=30)

    class Meta:
        model = Profile
        fields = ['email', 'name', 'initials', 'phone']