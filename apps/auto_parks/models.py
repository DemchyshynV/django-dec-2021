from django.db import models

from django.core.validators import RegexValidator

from apps.auto_parks.enums import RegEx


class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=20, validators=(RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg),))
