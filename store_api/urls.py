from django.urls import path
from .views import  *

urlpatterns = [
    path('category_list/', category_list),
    path('category/', category_create),
    path('category/<int:pk>/', category_detail),
    path('category/<int:pk>/update', category_update),
    path('category/<int:pk>/delete', category_delete),
    path('category/find/<str:name>/', category_filter),

    path('product_list/', product_list),
    path('product/', product_create),
    path('product/<int:pk>/', product_detail),
    path('product/<int:pk>/update', product_update),
    path('product/<int:pk>/delete', product_delete),
    path('product/find/<str:name>/<int:id>', product_filter),

    path('productsize_list/<int:product_id>', productSize_list),
    path('productsize/<int:pk>/', productSize_detail),
    path('productsize/<int:pk>/update', productSize_update),
    path('productsize/', productSize_create),
    path('productsize/<int:pk>/delete', productSize_delete),


    path('orderProductsize_list/', orderProductSize_list),
    path('orderProductsize/<int:pk>/', orderProductSize_detail),
    path('orderProductsize/<int:pk>/update', orderProductSize_update),
    path('orderProductsize/', orderProductSize_create),
    path('orderProductsize/<int:pk>/delete', orderProductSize_delete),

    path('order_list/', order_list),
    path('order/<int:pk>/', order_detail),
    path('order/<int:pk>/update', order_update),
    path('order/', order_create),
    path('order/<int:pk>/delete', order_delete),


    # path('order/', order_create),




]
