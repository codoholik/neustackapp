import threading

# customer_id -> cart
CARTS = {}

# order list
ORDERS = []

# coupon_code -> details
DISCOUNTS = {}

# statistics
TOTAL_DISCOUNT_GIVEN = 0

# order counter
ORDER_COUNT = 0

# lock for concurrency
ORDER_LOCK = threading.Lock()

# configuration
NTH_ORDER = 3
DISCOUNT_PERCENTAGE = 10
