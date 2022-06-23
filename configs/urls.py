from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars', include('apps.cars.urls'))
]

# localhost:8000/cars/ + те що в файлі urls.py cars
