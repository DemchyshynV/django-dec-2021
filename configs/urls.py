from django.contrib import admin
from django.urls import path
from users.views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users', UserListCreateView.as_view()),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view())
]
