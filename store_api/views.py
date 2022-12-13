from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import permission_required
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.
# CATEGORY

@api_view(["GET"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def category_detail(request, pk):
    if request.method == "GET":
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@permission_required('store_api.change_category')
@api_view(["PUT"])
def category_update(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_required('store_api.add_category')
@api_view(["POST"])
def category_create(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_required('store_api.delete_category')
@api_view(["DELETE"])
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def category_filter(request, name):
    try:
        categories = Category.objects.filter(name__contains=name)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

# PRODUCT

@api_view(["GET"])
def product_list(request):
    if request.method == "GET":
        poducts = Product.objects.all()
        serializer = ProductSerializer(poducts, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def product_detail(request, pk):
    if request.method == "GET":
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@permission_required('store_api.change_product')
@api_view(["PUT"])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_required('store_api.add_product')
@api_view(["POST"])
def product_create(request):
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_required('store_api.delete_product')
@api_view(["DELETE"])
def product_delete(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def product_filter(request, name, id):
    try:
        products = Product.objects.filter(name__contains=name)
        if id != 0:
            products = products.filter(category=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# PRODUCTSIZE

@api_view(["GET"])
def productSize_list(request, product_id):
    if request.method == "GET":
        productSizes = ProductSize.objects.filter(product=product_id)
        serializer = ProductSizeSerializer(productSizes, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def productSize_detail(request, pk):
    if request.method == "GET":
        try:
            productSize = ProductSize.objects.get(pk=pk)
        except ProductSize.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSizeSerializer(productSize)
        return Response(serializer.data)

@permission_required('store_api.change_productsize')
@api_view(["PUT"])
def productSize_update(request, pk):
    try:
        productSize = ProductSize.objects.get(pk=pk)
    except ProductSize.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ProductSizeSerializer(productSize, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_required('store_api.add_productsize')
@api_view(["POST"])
def productSize_create(request):
    if request.method == "POST":
        serializer = ProductSizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_required('store_api.delete_productsize')
@api_view(["DELETE"])
def productSize_delete(request, pk):
    try:
        productSize = ProductSize.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        productSize.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# order

# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# @api_view(["POST"])
# def order_create(request):
#     if request.method == "POST":
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def orderProductSize_list(request):
    if request.method == "GET":
        categories = OrderProductSize.objects.all()
        serializer = OrderProductSizeSerializer(categories, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def orderProductSize_detail(request, pk):
    if request.method == "GET":
        try:
            orderProductSize = OrderProductSize.objects.get(pk=pk)
        except OrderProductSize.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderProductSizeSerializer(orderProductSize)
        return Response(serializer.data)

@api_view(["PUT"])
def orderProductSize_update(request, pk):
    try:
        orderProductSize = OrderProductSize.objects.get(pk=pk)
    except OrderProductSize.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = OrderProductSizeSerializer(orderProductSize, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def orderProductSize_create(request):
    if request.method == "POST":
        serializer = OrderProductSizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def orderProductSize_delete(request, pk):
    try:
        orderProductSize = OrderProductSize.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        orderProductSize.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def order_list(request):
    if request.method == "GET":
        categories = Order.objects.all()
        serializer = OrderSerializer(categories, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def order_detail(request, pk):
    if request.method == "GET":
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

@api_view(["PUT"])
def order_update(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def order_create(request):
    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def order_delete(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
