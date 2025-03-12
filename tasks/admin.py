from django.contrib import admin

from tasks.models import AssignedTo, Subtask, Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'prio', 'created_date', 'due_date')
    search_fields = ('title', 'prio')
    list_filter = ('prio',)

class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'title')
    search_fields = ('task', 'title')
    list_filter = ('task',)

class AssignedToAdmin(admin.ModelAdmin):
    list_display = ('task', 'profile')
    search_fields = ('task', 'profile')
    list_filter = ('task',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask, SubtaskAdmin)
admin.site.register(AssignedTo, AssignedToAdmin)