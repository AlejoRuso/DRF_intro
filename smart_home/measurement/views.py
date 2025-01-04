from django.core.serializers import serialize
from rest_framework import generics
from rest_framework.response import Response

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer


class MeasurementsView(generics.ListCreateAPIView):

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SensorDetailView(generics.RetrieveUpdateAPIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = Sensor.objects.get(id=pk)
        serializer = SensorDetailSerializer(queryset)
        return Response(serializer.data, status=200)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = Sensor.objects.get(id=pk)
        serializer = SensorSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)


class SensorsView(generics.CreateAPIView):

    def get(self, request):
        queryset = Sensor.objects.all()
        serializer_class = SensorSerializer
        return Response(serializer_class(queryset, many=True).data, status=200)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)