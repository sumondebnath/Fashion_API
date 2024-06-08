from django.shortcuts import render
from rest_framework import viewsets
from review.serializers import ReviewSerializers
from review.models import Review

# Create your views here.

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def get_queryset(self):
        queryset = super().get_queryset()

        product_id = self.request.query_params.get("product_id")
        category_id = self.request.query_params.get("category_id")
        print(product_id)
        print(category_id)

        if product_id and category_id:
            queryset = queryset.filter(product_id=product_id, category_id=category_id)
        return queryset