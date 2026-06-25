from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ecommerce.serializers import (
    AddCartSerializer,
    CheckoutSerializer,
    GenerateDiscountSerializer
)

from ecommerce.services.cart_service import (
    CartService
)

from ecommerce.services.checkout_service import (
    CheckoutService
)

from ecommerce.services.discount_service import (
    DiscountService
)

from ecommerce.services.report_service import (
    ReportService
)


class AddToCartAPIView(APIView):

    def post(self, request):
        try:
            serializer = AddCartSerializer(
                data=request.data
            )

            serializer.is_valid(
                raise_exception=True
            )

            CartService.add_item(
                **serializer.validated_data
            )

            return Response(
                {
                    "message": "Item added"
                }
            )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class CartAPIView(APIView):

    def get(self, request, customer_id):

        cart = CartService.get_cart(
            customer_id
        )

        return Response(
            cart or {"items": []}
        )


class CheckoutAPIView(APIView):

    def post(self, request):
        try:
            serializer = CheckoutSerializer(
                data=request.data
            )

            serializer.is_valid(
                raise_exception=True
            )

            order = CheckoutService.checkout(
                serializer.validated_data[
                    "customer_id"
                ],
                serializer.validated_data.get(
                    "coupon_code"
                )
            )

            return Response(order)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class GenerateDiscountAPIView(APIView):

    def post(self, request):
        try:
            serializer = GenerateDiscountSerializer(
                data=request.data
            )

            serializer.is_valid(
                raise_exception=True
            )

            code = DiscountService.generate_coupon(applied_percentage=serializer.validated_data["discount_percentage"])

            return Response({
                "coupon": code
            })
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class StatsAPIView(APIView):

    def get(self, request):

        stats = (
            ReportService.get_stats()
        )

        return Response(stats)
