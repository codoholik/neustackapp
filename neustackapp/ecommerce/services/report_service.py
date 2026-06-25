from ecommerce.repository.store import (
    ORDERS,
    DISCOUNTS,
    TOTAL_DISCOUNT_GIVEN
)


class ReportService:

    @staticmethod
    def get_stats():

        total_items = 0
        revenue = 0

        for order in ORDERS:
            total_items += order["items"]
            revenue += order["final_amount"]

        return {
            "items_purchased": total_items,
            "revenue": revenue,
            "discount_codes": len(DISCOUNTS),
            "total_discount_given": TOTAL_DISCOUNT_GIVEN
        }