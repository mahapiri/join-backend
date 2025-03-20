
from encodings.punycode import T
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from tasks.api.serializers import AssignedToSerializer, SubtaskSerializer, TasksSerializer
from tasks.models import AssignedTo, Subtask, Task


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


class SubtaskViewset(viewsets.ModelViewSet):
    serializer_class = SubtaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Subtask.objects.filter(task_id=task_id).order_by('id')

    def perform_create(self, serializer):
        task = Task.objects.get(id=self.kwargs['task_id'])
        serializer.save(task=task)

    def create(self, request, *args, **kwargs):
        task = Task.objects.get(id=self.kwargs['task_id'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task=task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubtaskDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Subtask.objects.filter(task_id=task_id)

    def perform_update(self, serializer):
        task = Task.objects.get(id=self.kwargs['task_id'])
        serializer.save(task=task)

    def perform_destroy(self, instance):
        instance.delete()


class AssignedToViewSet(viewsets.ModelViewSet):
    queryset = AssignedTo.objects.all()
    serializer_class = AssignedToSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return AssignedTo.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task = Task.objects.get(id=self.kwargs['task_id'])
        serializer.save(task=task)

    def create(self, request, *args, **kwargs):
        task_id = self.kwargs['task_id']
        # Assuming profile data is passed in the request
        contact_data = request.data.get('contact')

        if not contact_data:
            return Response({"detail": "Contact is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the assigned-to entry
        assigned_to = AssignedTo.objects.create(
            task_id=int(task_id), contact_id=contact_data)

        # Use the serializer to return the created object
        serializer = AssignedToSerializer(assigned_to)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
