from django.urls import path, include
from rest_framework.routers import DefaultRouter
from category.views import CategoryViewsets

router = DefaultRouter()

router.register("list", CategoryViewsets)

urlpatterns =[
    path("", include(router.urls)),
]