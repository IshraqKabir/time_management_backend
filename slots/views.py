from rest_framework import viewsets
from .serializers import SlotSerializer
from .models import Slot
from url_filter.integrations.drf import DjangoFilterBackend

class SlotAPIView(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = '__all__'
    