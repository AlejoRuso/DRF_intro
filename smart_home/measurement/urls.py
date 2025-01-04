from django.urls import path
from .models import Measurement
from .views import  SensorsView, MeasurementsView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
]
