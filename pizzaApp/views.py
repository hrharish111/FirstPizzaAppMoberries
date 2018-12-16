from rest_framework import viewsets
from .models import Pizza,PizzaVariation,PizzaSize
from .serializers import PizzaSerializer,PizzaVariationSerializer,PizzaSizeSerializer


class PizzaViewSet(viewsets.ModelViewSet):
	queryset = Pizza.objects.all()
	serializer_class = PizzaSerializer


class PizzaVariationViewSet(viewsets.ModelViewSet):
    queryset = PizzaVariation.objects.all()
    serializer_class = PizzaVariationSerializer

class PizaSizeViesSet(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class =  PizzaSizeSerializer
