from django.urls import path
from rest_framework.routers import DefaultRouter
from tasks.api.views import SubtaskDetailViewSet, SubtaskViewset

# Router erstellen und den Viewset für Subtasks registrieren
router = DefaultRouter()
router.register(r'(?P<task_id>\d+)/subtasks', SubtaskViewset, basename='subtasks')



# Die URL-Patterns zurückgeben, die der Router verwaltet
urlpatterns = router.urls + [
    path('tasks/<int:task_id>/subtasks/<int:pk>/', SubtaskDetailViewSet.as_view(), name='subtask-detail'),
]