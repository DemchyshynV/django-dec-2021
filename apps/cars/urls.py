from django.urls import path

from .views import CarListCreateView, CarUpdateRetrieveDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarUpdateRetrieveDestroyView.as_view())
]
