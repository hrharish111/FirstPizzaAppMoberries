from rest_framework import mixins,viewsets
from .models import OrderItems,Order
from .serializers import OrderItemsSerializer,OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    """allows to add items and view items that was ordered"""
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

    def perform_create(self, serializer):
        customer_name = serializer.validated_data.pop('customer_name')
        customer_address = serializer.validated_data.pop('customer_address')
        order,created = Order.objects.get_or_create(customer_name=customer_name,status="progress",defaults={
            'customer_address':customer_address
        })
        serializer.save(order=order)

class OrderViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends= (DjangoFilterBackend,)
    filter_fields = ('customer_name','status')
