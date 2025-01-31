from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .models import Payments
from .serializers import PaymentSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    model = Payments
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "form_of_paymate"]
    orderind_fields = ["payment_date"]
