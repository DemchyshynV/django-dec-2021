from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')
    brand_end = filters.CharFilter(field_name='brand', lookup_expr='iendswith')
    brand_contains = filters.CharFilter(field_name='brand', lookup_expr='icontains')

    class Meta:
        model = CarModel
        fields = ('price_gt', 'price_lt', 'price_gte', 'brand_start', 'brand_end', 'brand_contains')
