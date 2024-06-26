from django.urls import path, include
from rest_framework.routers import DefaultRouter
from review.views import ReviewViewset

router = DefaultRouter()

router.register("list", ReviewViewset)

urlpatterns = [
    path("", include(router.urls)),
]