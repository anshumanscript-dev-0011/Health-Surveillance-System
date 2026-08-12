import logging

from rest_framework import serializers

from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


logger = logging.getLogger(__name__)


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            "username",
            "email",
            "password",
            "role",
            "phone_number",
        )

        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 8,
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )

        logger.info(
            "User registered successfully: username=%s, role=%s",
            user.username,
            user.role,
        )

        return user

class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        logger.info(
            "Login attempt received for username=%s",
            attrs.get("username"),
        )

        data = super().validate(attrs)

        user = self.user

        logger.info(
            "User logged in successfully: username=%s, role=%s",
            user.username,
            user.role,
        )

        data["user"] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
        }

        return data