from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response

from apps.cars.serializers import CarSerializer

from .models import AutoParksModel
from .serializers import AutoParkSerializer


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParksRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


# class AutoParkAddCarView(CreateAPIView):
#     queryset = AutoParksModel
#     serializer_class = CarSerializer
#
#     def perform_create(self, serializer):
#         auto_park = self.get_object()
#         serializer.save(auto_park=auto_park)

class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParksModel
    serializer_class = CarSerializer

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        car = self.request.data
        serializer = self.serializer_class(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        return Response(serializer.data, status.HTTP_201_CREATED)
