from django.urls import path
from .views import  *

urlpatterns = [
    path('category_list/', category_list),
    path('category/', category_create),
    path('category/<int:pk>/', category_detail),
    path('category/<int:pk>/update', category_update),
    path('category/<int:pk>/delete', category_delete),
    path('category/find/<str:name>/', category_filter),

]
