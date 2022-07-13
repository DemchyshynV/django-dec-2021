from django_filters import rest_framework as filters

from .models import AutoParksModel


class AutoParkFilter(filters.FilterSet):
    cars_year_lt = filters.NumberFilter(field_name='cars', lookup_expr='year__lt')

    class Meta:
        model = AutoParksModel
        fields = ('cars_year_lt',)
