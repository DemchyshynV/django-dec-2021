from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView

from .models import AutoParksModel
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParksRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParksModel
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
