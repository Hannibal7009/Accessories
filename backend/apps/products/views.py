from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductList(generics.ListAPIView):
    queryset = Product.objects.order_by(
        'created_at').reverse().filter(status='active')
    serializer_class = ProductSerializer
