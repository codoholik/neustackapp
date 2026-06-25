from ecommerce.repository.store import CARTS


class CartService():

    @staticmethod
    def add_item(customer_id, product_id, quantity, price):

        if customer_id not in CARTS:
            CARTS[customer_id] = {
                "items": []
            }

        CARTS[customer_id]["items"].append({
            "product_id": product_id,
            "quantity": quantity,
            "price": price
        })

    @staticmethod
    def get_cart(customer_id):
        return CARTS.get(customer_id)

    @staticmethod
    def clear_cart(customer_id):
        CARTS.pop(customer_id, None)