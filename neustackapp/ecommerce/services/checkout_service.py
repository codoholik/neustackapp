import uuid

from ecommerce.repository.store import (
    CARTS,
    ORDERS,
    ORDER_COUNT,
    ORDER_LOCK,
    NTH_ORDER,
    TOTAL_DISCOUNT_GIVEN,
    DISCOUNT_PERCENTAGE
)

from ecommerce.services.discount_service import (
    DiscountService
)

from ecommerce.services.cart_service import (
    CartService
)


class CheckoutService():

    @staticmethod
    def checkout(customer_id, coupon_code=None, discount_percentage=DISCOUNT_PERCENTAGE):

        cart = CARTS.get(customer_id)

        if not cart:
            raise Exception("Cart is empty")

        total = 0
        total_items = 0

        for item in cart["items"]:
            total += (
                item["price"] * item["quantity"]
            )

            total_items += item["quantity"]

        discount = 0

        if coupon_code:
            discount = DiscountService.apply_coupon(
                coupon_code,
                total
            )

        final_amount = total - discount

        with ORDER_LOCK:

            ORDER_COUNT += 1
            order_number = ORDER_COUNT

            generated_coupon = None

            if order_number % NTH_ORDER == 0:
                generated_coupon = (
                    DiscountService.generate_coupon(applied_percentage=discount_percentage)
                )

        order = {
            "order_id": str(uuid.uuid4()),
            "customer_id": customer_id,
            "total": total,
            "discount": discount,
            "final_amount": final_amount,
            "items": total_items
        }

        ORDERS.append(order)

        TOTAL_DISCOUNT_GIVEN += discount

        CartService.clear_cart(customer_id)

        return order