from django.urls import path

from .views import AddOwnerToAutoParkView, AutoParkAddCarView, AutoParksListCreateView, AutoParksRetrieveDestroyView

urlpatterns = [
    path('', AutoParksListCreateView.as_view()),
    path('/<int:pk>', AutoParksRetrieveDestroyView.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view()),
    path('/<int:pk>/add_owner/<int:user_id>', AddOwnerToAutoParkView.as_view())
]
