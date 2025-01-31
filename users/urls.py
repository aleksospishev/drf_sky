from rest_framework.routers import SimpleRouter

from .views import PaymentsViewSet

app_name = "users"

router_payment = SimpleRouter()

router_payment.register("payment", PaymentsViewSet)

urlpatterns = router_payment.urls + []
