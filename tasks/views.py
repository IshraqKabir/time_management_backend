from rest_framework import viewsets
from .serializers import TaskSerializer
from url_filter.integrations.drf import DjangoFilterBackend
from tasks.models import Task

class TaskAPIView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = '__all__'

    