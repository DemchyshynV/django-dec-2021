from django.urls import path

from .views import AddAvatarView, UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view())

]
