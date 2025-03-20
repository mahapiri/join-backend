
from rest_framework import serializers
from contacts.models import Contact


class ContactsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)
    phone = serializers.CharField(max_length=30)
    color = serializers.CharField(max_length=100)

    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)