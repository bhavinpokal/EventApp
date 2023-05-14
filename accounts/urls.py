from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserLoginAPIView, UserRegistrationAPIView

urlpatterns = [
    path("user-register/", UserRegistrationAPIView.as_view(), name="users"),
    path("user-login/", UserLoginAPIView.as_view(), name="user-login"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
