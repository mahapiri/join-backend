from email.policy import default
from rest_framework import serializers
from tasks.models import CATEGORY_CHOICES, PRIO_CHOICES, STATUS_CHOICES, Subtask, Task


class TasksSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=STATUS_CHOICES, default="to_do")
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    due_date = serializers.DateField(required=True)
    prio = serializers.CharField(required=False, allow_blank=True, default="low")
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Task
        fields = ['id', 'status', 'title', 'description', 'due_date', 'prio', 'category', 'created_date']

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def validate_prio(self, value):
        return value if value else "low"
    
class SubtaskSerializer(serializers.ModelSerializer):
    task_title = serializers.CharField(source="task.title", read_only=True)
    class Meta:
        model = Subtask
        fields = ['id', 'task', 'title', 'task_title']