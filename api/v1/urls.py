from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1 import views

app_name = 'v1'
router = DefaultRouter()

router.register(r'orders', views.Order, basename='orders')

urlpatterns = [
    path("orders/<int:pk>/pay/", views.Order.as_view(), name="order_payment"),
]