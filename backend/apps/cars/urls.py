from django.urls import path

from .views import CarListView, CarUpdateRetrieveDestroyView

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>', CarUpdateRetrieveDestroyView.as_view())
]
