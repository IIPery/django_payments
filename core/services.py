import stripe
from django.conf import settings
from core.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment_intent(order: Order):
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(order.get_total_price() * 100),
            currency='usd',
            description=f"Оплата заказа {order.id}",
        )
        return intent.client_secret
    except Exception as e:
        raise Exception(f"Ошибка при создании PaymentIntent: {str(e)}")