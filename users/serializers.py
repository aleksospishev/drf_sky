from rest_framework import serializers

from .models import Payments, User


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "phone", "city", "avatar", "is_active", "password")
