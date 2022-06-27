from django.urls import path, include


urlpatterns = [
    path('computers', include('apps.computers.urls'))
]
