from django.urls import path

from products.apps import ProductsConfig
from products.views import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductRetrieveAPIView,
    ProductDestroyAPIView,
    ProductUpdateAPIView,
)

app_name = ProductsConfig.name

urlpatterns = [
    path("product/", ProductListAPIView.as_view(), name="product-list"),
    path("product/create/", ProductCreateAPIView.as_view(), name="product-create"),
    path(
        "product/detail/<int:pk>/",
        ProductRetrieveAPIView.as_view(),
        name="product-detail",
    ),
    path(
        "product/delete/<int:pk>/",
        ProductDestroyAPIView.as_view(),
        name="product-delete",
    ),
    path(
        "product/update/<int:pk>/",
        ProductUpdateAPIView.as_view(),
        name="product-update",
    ),
]
