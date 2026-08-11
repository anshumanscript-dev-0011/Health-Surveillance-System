from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        STATE_ADMIN = "STATE_ADMIN", "State Admin"
        DISTRICT_ADMIN = "DISTRICT_ADMIN", "District Admin"
        DOCTOR = "DOCTOR", "Doctor"
        LAB_TECHNICIAN = "LAB_TECHNICIAN", "Lab Technician"
        ASHA_WORKER = "ASHA_WORKER", "ASHA Worker"
        DATA_ENTRY_OPERATOR = "DATA_ENTRY_OPERATOR", "Data Entry Operator"

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.DATA_ENTRY_OPERATOR,
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"