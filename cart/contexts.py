#!/usr/bin/python
# -*- coding: utf-8 -*-

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import ProductVariant


def cart_content(request):
    """
    Provide Cart-Content throughout the whole website
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    for item_id, item_data in cart.items():
        productvariant_id = item_id
        lineitem = get_object_or_404(ProductVariant, pk=item_id)
        for item_id, item_data in cart[item_id].items():
            if item_id == 'qty':
                quantity = item_data

        if lineitem.product.is_on_sale or lineitem.product.avail_for_pre_order:
            price = lineitem.product.discount_price
        else:
            price = lineitem.product.price

        total += price * quantity
        product_count += quantity
        subtotal = price * quantity
        cart_items.append({
            'productvariant': productvariant_id,
            'quantity': quantity,
            'lineitem': lineitem,
            'subtotal': subtotal,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_FEE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = Decimal(delivery) + Decimal(total)

    total_tax = Decimal(grand_total) * \
        Decimal(settings.TAX_RATE_PERCENTAGE / 100)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'total_tax': total_tax,
        'tax_rate': settings.TAX_RATE_PERCENTAGE,
    }

    return context
