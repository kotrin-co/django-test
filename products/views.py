from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDummyApiView(APIView):
  def get(self, request, format=None):
    return Response({"name": "kentaro!!"})

@api_view(['GET'])
def product_list(request):

  if request.method == 'GET':
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)