from rest_framework import serializers
from tasks.models import Task


class TasksSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    due_date = serializers.DateField()
    prio = serializers.CharField(max_length=10)
    category = serializers.CharField(max_length=20)
    created_date = serializers.DateField()

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'prio', 'category', 'created_date']

    def create(self, validated_data):
        return Task.objects.create(**validated_data)