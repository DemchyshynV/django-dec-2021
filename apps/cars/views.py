from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CarModel
from .serializers import CarSerializer


# CRUD
# Create
# Read/Retrieve
# Update
# Delete/Destroy

class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        # instance = CarModel.objects.create(**data)
        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarUpdateRetrieveDestroyView(APIView):
    def get(self, *args, **kwargs):
        car_id = kwargs.get('pk')

        if not CarModel.objects.filter(pk=car_id).exists():
            return Response('Car with this id is not found!!!!', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car with this id is not found!!!!', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car, data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car with this id is not found!!!!', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car with this id is not found!!!!', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
