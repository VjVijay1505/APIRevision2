from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle

from django_filters.rest_framework import DjangoFilterBackend

from products.models import ProductModel
from .serializer import ProductSerializer

class itemsearch(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'price']
    

class items(APIView):
    
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'items_throttle'
    
    
    def get(self, request):
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
        
class item(APIView):
    
    permission_classes = [IsAuthenticated]    
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'item_throttle'
    
    def get(self, request, pk):
        product = ProductModel.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        product = ProductModel.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        product = ProductModel.objects.get(id=pk)
        product.delete()
        return Response({'Message': 'Product deleted successfully'}, status=status.HTTP_200_OK)