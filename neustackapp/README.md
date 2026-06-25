# Ecommerce Store API

A simple ecommerce backend application built using **Python, Django, and Django REST Framework**.

The application allows customers to:

* Add items to their cart
* Checkout and place orders
* Apply discount coupons
* Automatically generate discount coupons for every nth order
* View administrative statistics

The application uses **in-memory storage** as specified in the assignment requirements.

---

## Tech Stack

* Python 3.12
* Django 5.x
* Django REST Framework
* Pytest
* In-memory storage

---

## Features

### Customer APIs

* Add items to cart
* View cart
* Checkout order
* Apply discount coupon

### Admin APIs

* Generate discount coupon
* View purchase statistics

### Additional Features

* Every nth order receives a coupon.
* Single-use discount coupons.
* Thread-safe checkout logic.
* Service and repository layers.
* Unit-testable business logic.

---

## Project Structure

```text
ecommerce/
│
├── ecommerce/
│   ├── settings.py
│   └── urls.py
│
├── store/
│   ├── repositories/
│   │   └── memory_store.py
│   │
│   ├── services/
│   │   ├── cart_service.py
│   │   ├── checkout_service.py
│   │   ├── discount_service.py
│   │   └── report_service.py
│   │
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── DECISIONS.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ecommerce
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python manage.py runserver
```

Application will start at:

```text
http://127.0.0.1:8000/
```

---

## API Endpoints

| Method | Endpoint                   | Description      |
| ------ | -------------------------- | ---------------- |
| POST   | `/api/cart/items/`         | Add item to cart |
| GET    | `/api/cart/<customer_id>/` | View cart        |
| POST   | `/api/checkout/`           | Checkout cart    |
| POST   | `/api/admin/discount/`     | Generate coupon  |
| GET    | `/api/admin/stats/`        | View statistics  |

---

# API Examples

## 1. Add Item To Cart

### Request

```http
POST /api/cart/items/
```

```json
{
    "customer_id": "cust1",
    "product_id": "P1",
    "quantity": 2,
    "price": 500
}
```

### Response

```json
{
    "message": "Item added"
}
```

---

## 2. View Cart

### Request

```http
GET /api/cart/cust1/
```

### Response

```json
{
    "items": [
        {
            "product_id": "P1",
            "quantity": 2,
            "price": 500
        }
    ]
}
```

---

## 3. Checkout

### Request

```http
POST /api/checkout/
```

```json
{
    "customer_id": "cust1",
    "coupon_code": "DISC-ABCD12"
}
```

### Response

```json
{
    "order_id": "c7855b90-24df-4d58-bf96-d0ad640c52b2",
    "customer_id": "cust1",
    "total": 1000,
    "discount": 100,
    "final_amount": 900
}
```

---

## 4. Generate Discount Coupon

### Request

```http
POST /api/admin/discount/
```

```json
{
    "discount_percentage": 25
}
```

### Response

```json
{
    "coupon": "DISC-ABCD12"
}
```

---

## 5. Statistics API

### Request

```http
GET /api/admin/stats/
```

### Response

```json
{
    "items_purchased": 12,
    "revenue": 8500,
    "discount_codes": 4,
    "total_discount_given": 500
}
```

---

# Business Rules

1. Customers can add multiple items to their cart.
2. Discount coupons are optional during checkout.
3. Coupons can only be used once.
4. Every nth successful order generates a coupon.
5. Coupons apply to the entire order amount.
6. Cart is cleared after successful checkout.

---

# Assumptions

* One active cart per customer.
* Coupons do not expire.
* Coupons are single-use.
* Orders are processed sequentially.
* In-memory storage is acceptable according to assignment requirements.

---

# Concurrency Handling

Checkout operations use thread locking to prevent race conditions.

This ensures:

* Correct order numbering.
* Proper nth-order coupon generation.
* Prevention of duplicate coupon generation.

---

# Running Tests

```bash
pytest tests/
```

---

# Future Improvements

If this application were extended for production usage:

* PostgreSQL for persistent storage
* Redis for cart management
* Celery for asynchronous processing
* Authentication and authorization
* Distributed locking
* API versioning
* Rate limiting
* Monitoring and observability
* Idempotent checkout requests
