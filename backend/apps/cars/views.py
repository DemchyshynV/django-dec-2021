from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from core.permissions.user_permossions import IsSuperUser

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter

    def get_queryset(self):
        print(self.request.user.id)
        qs = self.queryset.all()
        price_gt = self.request.query_params.get('price_gt')
        auto_park_id = self.request.query_params.get('autoParkId')

        if price_gt:
            qs = qs.filter(price__gt=price_gt)

        if auto_park_id:
            qs = qs.filter(auto_park_id=auto_park_id)
        return qs


class CarUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get one Car
    put:
        Update car
    delete:
        Delete car
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)
