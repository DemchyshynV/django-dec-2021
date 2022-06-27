from django.urls import path

from .views import ComputerListCreateView, ComputerRetrieveUpdateDestroyView

urlpatterns = [
    path('', ComputerListCreateView.as_view()),
    path('/<int:pk>', ComputerRetrieveUpdateDestroyView.as_view())
]
