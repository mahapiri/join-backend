from rest_framework import serializers
from tasks.models import Subtask, Task


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
    
class SubtaskSerializer(serializers.ModelSerializer):
    task_title = serializers.CharField(source="task.title", read_only=True)
    class Meta:
        model = Subtask
        fields = ['id', 'task', 'title', 'task_title']