from django.db import models
from profiles.models import Profile

STATUS_CHOICES = [
    ("to_do", "To do"),
    ("in_progress", "In progress"),
    ("await_feedback", "Await feedback"),
    ("done", "Done"),
]

PRIO_CHOICES = [
    ("urgent", "Urgent"),
    ("medium", "Medium"),
    ("low", "Low"),
]

CATEGORY_CHOICES = [
    ("technical_task", "Technical Task"),
    ("user_story", "User Story"),
]

# Create your models here.


class Task(models.Model):
    status = models.CharField(max_length=50, choices=STATUS_CHOICES ,null=False, blank=True, default="to_do")
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    due_date = models.DateField(null=False, blank=False)
    prio = models.CharField(max_length=10, choices=PRIO_CHOICES, default="low")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=False, blank=False, default="user_story")
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title
    
    def get_assigned_to(self):
        profiles = [assignment.profile for assignment in self.assignedto_set.all()]
        return ", ".join(str(profile) for profile in profiles) if profiles else "Keine Profile vorhanden"

    def get_subtasks(self):
        return ", ".join(subtask.title for subtask in self.subtasks.all()) if self.subtasks.exists() else "keine Subtasks"

class AssignedTo(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="assignments")
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="assignments")

    class Meta:
        verbose_name = "Assigned To"
        verbose_name_plural = "Assigned To"
    
    def __str__(self):
        return f"{self.task.title}: {self.profile}"

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Subtask"
        verbose_name_plural = "Subtasks"

    def __str__(self):
        return f"{self.task.title}: {self.title}"