from ecommerce.services.cart_service import CartService
from ecommerce.services.checkout_service import CheckoutService


def test_checkout():
    CartService.add_item(
        customer_id="user1",
        product_id="p1",
        quantity=2,
        price=100
    )

    order = CheckoutService.checkout(
        customer_id="user1"
    )

    assert order["final_amount"] == 200