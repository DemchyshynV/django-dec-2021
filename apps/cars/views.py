from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from .models import CarModel
from .serializers import CarSerializer


# class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get_queryset(self):
#         price_gt = self.request.query_params.get('price_gt')
#         if price_gt:
#             return self.queryset.filter(price__gt=price_gt)
#         return super().get_queryset()
#
#     def get(self, *args, **kwargs):
#         return super().list(self.request, *args, **kwargs)
#
#     # qs = self.get_queryset()
#         # # qs=qs.filter(brand__in=('bmw', 'audi', 'kia'))
#         # # qs = qs.filter(brand__icontains='di')
#         # # qs = qs.filter(price__range=(4000, 6000))
#         # # qs = qs.filter(price__in=(2000, 2500, 3255,  6000))
#         # # qs = qs.filter(price__)
#         # # qs = qs.filter(Q(price=4000) | Q(price=1000) | Q(brand='bmw'))
#         # # qs = qs.filter(Q(brand='bmw'), (Q(price=6000) | Q(price=1000)))
#         # # qs = qs.filter(price__gt=500).order_by('price', '-year').reverse().exclude(brand='bmw')
#         # # print(qs.query)
#         # # print(qs.count())
#         # # price_gt = self.request.query_params.get('price_gt')
#         # #
#         # # if price_gt:
#         # #     qs = qs.filter(price__gt=price_gt)
#         #
#         # serializer = self.serializer_class(qs, many=True)
#         # return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         return super().create(self.request, *args, **kwargs)
# data = self.request.data
# # instance = CarModel.objects.create(**data)
# serializer = CarSerializer(data=data)
# if not serializer.is_valid():
#     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
# serializer.save()
# print(serializer.data)
# return Response(serializer.data, status.HTTP_201_CREATED)


# class CarUpdateRetrieveDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         return super().retrieve(self.request, *args, **kwargs)
#
#     # # car_id = kwargs.get('pk')
#         # #
#         # # if not CarModel.objects.filter(pk=car_id).exists():
#         # #     return Response('Car with this id is not found!!!!', status.HTTP_404_NOT_FOUND)
#         # #
#         # # car = CarModel.objects.get(pk=car_id)
#         # car = self.get_object()
#         # serializer = self.serializer_class(car)
#         # return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         return super().update(self.request, *args, **kwargs)
#
#     # data = self.request.data
#         # pk = kwargs.get('pk')
#         #
#         # if not CarModel.objects.filter(pk=pk).exists():
#         #     return Response('Car with this id is not found!!!!', status.HTTP_404_NOT_FOUND)
#         #
#         # car = CarModel.objects.get(pk=pk)
#         # serializer = CarSerializer(car, data)
#         #
#         # # if not serializer.is_valid():
#         # #     return Response(serializer.errors)
#         #
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         return super().partial_update(self.request, *args, **kwargs)
#
#     # data = self.request.data
#         # pk = kwargs.get('pk')
#         #
#         # if not CarModel.objects.filter(pk=pk).exists():
#         #     return Response('Car with this id is not found!!!!', status.HTTP_404_NOT_FOUND)
#         #
#         # car = CarModel.objects.get(pk=pk)
#         # serializer = CarSerializer(car, data, partial=True)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         return super().destroy(self.request, *args, **kwargs)
# # pk = kwargs.get('pk')
#         #
#         # if not CarModel.objects.filter(pk=pk).exists():
#         #     return Response('Car with this id is not found!!!!', status.HTTP_404_NOT_FOUND)
#         #
#         # car = CarModel.objects.get(pk=pk)
#         # car.delete()
#         # return Response(status=status.HTTP_204_NO_CONTENT)
class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        price_gt = self.request.query_params.get('price_gt')
        if price_gt:
            return self.queryset.filter(price__gt=price_gt)
        return super().get_queryset()


class CarUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
