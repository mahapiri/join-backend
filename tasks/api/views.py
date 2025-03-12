
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from tasks.api.serializers import TasksSerializer
from tasks.models import Task


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('pk')
    serializer_class = TasksSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all().order_by('pk')
    serializer_class = TasksSerializer
    permission_classes = [AllowAny]