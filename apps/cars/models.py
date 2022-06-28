from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator
from apps.auto_parks.models import AutoParksModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # brand = models.CharField(max_length=100, null=True, validators=(MinLengthValidator(5), MaxLengthValidator(10)))
    # price = models.IntegerField(validators=(MinValueValidator(100000),))
    # year = models.IntegerField()
    # create_at = models.DateTimeField(auto_now_add=True)
    # update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand
