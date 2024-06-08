from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import UserAccountViewsets, UserAddressViesets, RegistrationViewset, LoginViewset, LogoutViewset, ChangePasswordViewset

router = DefaultRouter()

router.register("details", UserAccountViewsets)
router.register("address", UserAddressViesets)

urlpatterns = [
    path("", include(router.urls)),
    path("registration/", RegistrationViewset.as_view(), name="register"),
    path("login/", LoginViewset.as_view(), name="login"),
    path("change_password/", ChangePasswordViewset.as_view(), name="changePassword"),
    path("logout/", LogoutViewset.as_view(), name="logout"),
]