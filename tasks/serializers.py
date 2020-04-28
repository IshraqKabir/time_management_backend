from rest_framework import serializers
from .models import Task
from slots.models import Slot

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'