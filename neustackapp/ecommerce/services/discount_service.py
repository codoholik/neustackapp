import uuid
from ecommerce.repository.store import DISCOUNTS


class DiscountService():

    @staticmethod
    def generate_coupon(applied_percentage):

        code = f"DISC-{uuid.uuid4()}"

        DISCOUNTS[code] = {
            "percentage": applied_percentage,
            "used": False
        }

        return code

    @staticmethod
    def validate_coupon(code):

        coupon = DISCOUNTS.get(code)

        if not coupon:
            raise Exception("Invalid coupon")

        if coupon["used"]:
            raise Exception("Coupon already used")

        return coupon

    @staticmethod
    def apply_coupon(code, total):

        coupon = DiscountService.validate_coupon(code)

        discount = (
            total * coupon["percentage"]
        ) / 100

        coupon["used"] = True

        return discount