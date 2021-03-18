from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.parsers import (MultiPartParser, FormParser,
                                    JSONParser, FileUploadParser)
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Image, Order, Favourite
from .filters import ProdutcFilter
from .serializers import ProductSerializer, \
                         ImageSerializer, \
                         OrderSerializer, FavouriteSerializer
from .permissions import ProductPermission


class OrderCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = None

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class FavouriteCreateView(generics.ListCreateAPIView):
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
    pagination_class = None


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [ProductPermission]
    filter_class = ProdutcFilter
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ["name"]
    
    def perform_create(self, serializer):
        obj = serializer.save(seller=self.request.user)


class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # parser_classes = (MultiPartParser,FormParser,JSONParser, FileUploadParser)
