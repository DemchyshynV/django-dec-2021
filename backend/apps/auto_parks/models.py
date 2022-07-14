from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from apps.auto_parks.enums import RegEx

UserModel = get_user_model()


class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['id']

    name = models.CharField(max_length=20, validators=(RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg),))
    owners = models.ManyToManyField(UserModel, related_name='auto_parks')
