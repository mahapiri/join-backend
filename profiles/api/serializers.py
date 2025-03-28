from django.contrib.auth.models import User
from rest_framework import serializers
from profiles.models import Profile

class ProfilesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    email = serializers.EmailField(source="user.email", write_only=True)  
    password = serializers.CharField(source="user.password", write_only=True, style={'input_type': 'password'})
    initials = serializers.CharField(read_only=True)
    phone = serializers.CharField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)  

    class Meta:
        model = Profile
        fields = ['email', 'password', 'name', 'initials', 'phone', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        email = user_data['email']
        password = user_data['password']
        full_name = validated_data.pop('name')
        
        name_parts = full_name.strip().split(" ", 1)
        first_name = name_parts[0] if len(name_parts) > 0 else ""
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)

        profile = Profile.objects.create(user=user, **validated_data)
        return profile
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['email'] = instance.user.email
        representation['name'] = instance.name
        return representation
