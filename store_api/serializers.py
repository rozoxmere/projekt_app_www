from rest_framework import serializers
from .models import Order, Category, OrderProductSize, Product, ProductSize

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(required = True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

    def validate_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Nazwa categorii powinna zaczynać się z dużej litery!"
            )
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "category"]
        read_only_fields = ["id"]

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ["size", "amount", "product"]
        read_only_fields = ["id"]


class OrderProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductSize
        fields = ["product_size", "amount_in_order",]
        read_only_fields = ["id"]



# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ["user", "orderProductSize", "order_date"]

#     orderProductSize = OrderProductSizeSerializer(many=True)

#     def create(self, validated_data):
#         products_data = validated_data.pop("orderProductSize")
#         order = Order.objects.create(**validated_data)
#         for product_data in products_data:
#             print(product_data)
#             self.set([product_data])
#             OrderProductSize.objects.create(**product_data)
#         return order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user", "orderProductSize", "order_date"]

    def create(self, validated_data):
        bought_products = validated_data["orderProductSize"]
        flags = 0
        for element in bought_products:
            print(f"Id : {element.product_size.id} {element.product_size.amount} |||| {element.amount_in_order} ")
            difference = element.product_size.amount - element.amount_in_order
            if difference < 0:
                flags = 1
        if flags is not 1:
            for element in bought_products:
                ProductSize.objects.get(pk=element.product_size.id).amount = element.product_size.amount - element.amount_in_order

        return validated_data