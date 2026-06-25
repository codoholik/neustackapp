from django.urls import path

from ecommerce.views import (
    AddToCartAPIView,
    CartAPIView,
    CheckoutAPIView,
    GenerateDiscountAPIView,
    StatsAPIView
)

urlpatterns = [

    path(
        "cart/items/",
        AddToCartAPIView.as_view()
    ),

    path(
        "cart/<str:customer_id>/",
        CartAPIView.as_view()
    ),

    path(
        "checkout/",
        CheckoutAPIView.as_view()
    ),

    path(
        "admin/discount/",
        GenerateDiscountAPIView.as_view()
    ),

    path(
        "admin/stats/",
        StatsAPIView.as_view()
    ),
]