from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions.user_permossions import IsSuperUser

from .serializers import AddAvatarSerializer, UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class AddAvatarView(UpdateAPIView):
    http_method_names = ('patch',)
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile


class UserToAdminView(GenericAPIView):
    queryset = UserModel
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(UserToAdminView):

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)
