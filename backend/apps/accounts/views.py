import logging

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer, LoginSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


logger = logging.getLogger(__name__)


class RegisterAPIView(generics.CreateAPIView):

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        logger.info(
            "Registration request received."
        )

        response = super().create(
            request,
            *args,
            **kwargs
        )

        logger.info(
            "Registration request completed successfully."
        )

        return response

class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
