from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("cart/", views.Cart.as_view(), name="cart"),
    path("add_to_cart/<int:item_id>/", views.AddToCart.as_view(), name="add_to_cart"),
    path('order/success/<int:order_id>/', views.PaymentSuccess.as_view(), name='payment_success'),
]