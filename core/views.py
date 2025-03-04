from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from core import models, consts


class Index(View):
    def get(self, request):
        items = models.Item.objects.all()
        return render(request, 'core/index.html', {'items': items})


class AddToCart(View):
    def post(self, request, item_id):
        item = get_object_or_404(models.Item, id=item_id)

        order, created = models.Order.objects.get_or_create(status=consts.STATUS_PENDING)

        if item not in order.items.all():
            order.items.add(item)

        order.save()
        return redirect('core:cart')


class Cart(View):
    def get(self, request):
        order, _ = models.Order.objects.get_or_create(status=consts.STATUS_PENDING)
        discounts = models.Discount.objects.all()
        taxes = models.Tax.objects.all()

        return render(
            request,
            'core/cart.html',
            {
                'order': order,
                'discounts': discounts,
                'taxes': taxes,
                'stripe_public_key': settings.STRIPE_PUBLIC_KEY
            }
        )

    def post(self, request):
        order, _ = models.Order.objects.get_or_create(status=consts.STATUS_PENDING)

        if 'discount_id' in request.POST:
            discount = get_object_or_404(models.Discount, id=request.POST['discount_id'])
            order.discount = discount

        if 'tax_id' in request.POST:
            tax = get_object_or_404(models.Tax, id=request.POST['tax_id'])
            order.tax = tax

        order.save()
        return redirect('core:cart')


class PaymentSuccess(View):
    def get(self, request, order_id):
        order = get_object_or_404(models.Order, id=order_id)
        order.status = consts.STATUS_PAID
        order.save()
        return render(request, 'core/payment_success.html', {'order': order})