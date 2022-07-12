from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')

    class Meta:
        model = CarModel
        fields = ('price', 'brand')
