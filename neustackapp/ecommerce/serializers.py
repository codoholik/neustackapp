from rest_framework import serializers


class AddCartSerializer(serializers.Serializer):
    customer_id = serializers.CharField()
    product_id = serializers.CharField()
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=1)


class CheckoutSerializer(serializers.Serializer):
    customer_id = serializers.CharField()
    coupon_code = serializers.CharField(required=False, allow_blank=True)


class GenerateDiscountSerializer(serializers.Serializer):
    discount_percentage = serializers.FloatField(min_value=1)
