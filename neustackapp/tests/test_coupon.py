from ecommerce.repository.store import DISCOUNT_PERCENTAGE

from ecommerce.services.discount_service import (
    DiscountService
)


def test_coupon():
    code = (
        DiscountService.generate_coupon(applied_percentage=DISCOUNT_PERCENTAGE)
    )

    coupon = (
        DiscountService.validate_coupon(code)
    )

    assert coupon["percentage"] == DISCOUNT_PERCENTAGE
    assert coupon["used"] == False