from django.urls import path

from .views import AutoParksListCreateView, AutoParkAddCarView, AutoParksRetrieveDestroyView

urlpatterns = [
    path('', AutoParksListCreateView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>', AutoParksRetrieveDestroyView.as_view(), name='auto_parks_retrieve_destroy'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='auto_parks_add_car')
]
