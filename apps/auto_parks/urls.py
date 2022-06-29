from django.urls import path

from .views import AutoParksListCreateView, AutoParkAddCarView, AutoParksRetrieveDestroyView

urlpatterns = [
    path('', AutoParksListCreateView.as_view()),
    path('/<int:pk>', AutoParksRetrieveDestroyView.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view())
]
