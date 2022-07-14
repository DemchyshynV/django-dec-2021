from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

UserModel = get_user_model()


class EmailSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email',)
        extra_kwargs = {
            'email': {
                'validators': []
            }
        }


class PasswordSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)
