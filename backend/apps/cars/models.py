from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from apps.auto_parks.models import AutoParksModel

from .enums import RegEx
from .managers import CarManager


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        ordering = ['id']

    brand = models.CharField(max_length=100, validators=(RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.msg),))
    price = models.IntegerField(validators=(MinValueValidator(0), MaxValueValidator(1000000)))
    year = models.IntegerField(validators=(MinValueValidator(1990), MaxValueValidator(date.today().year)))
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = CarManager()

    def __str__(self):
        return self.brand
