from django.urls import path

from .views import AddAvatarView, UserListCreateView, UserToAdminView, AdminToUserView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view()),

]
