from django.core.validators import RegexValidator
from django.db import models

from apps.auto_parks.enums import RegEx


class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['id']

    name = models.CharField(max_length=20, validators=(RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg),))
