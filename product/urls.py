from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewset

router = DefaultRouter()

router.register("list", ProductViewset)

urlpatterns = [
    path("", include(router.urls)),
]