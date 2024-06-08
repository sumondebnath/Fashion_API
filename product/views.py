from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from product.serializers import ProductSerializer
from product.models import Product

# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["category__name", "name", "product_number", "brand_number", "size", "product_type", "gender_type", "description"]

    def get_queryset(self):
        queryset = super().get_queryset()

        category_id = self.request.query_params.get("category_id")
        # print(category_id)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset