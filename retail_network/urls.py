from django.urls import path
from retail_network.apps import RetailNetworkConfig
from retail_network.views import (
    Retail_networkListAPIView,
    Retail_networkCreateAPIView,
    Retail_networkRetrieveAPIView,
    Retail_networkDestroyAPIView,
    Retail_networkUpdateAPIView,
)

app_name = RetailNetworkConfig.name


urlpatterns = [
    path("retail/", Retail_networkListAPIView.as_view(), name="retail-list"),
    path("retail/create/", Retail_networkCreateAPIView.as_view(), name="retail-create"),
    path(
        "retail/detail/<int:pk>/",
        Retail_networkRetrieveAPIView.as_view(),
        name="retail-detail",
    ),
    path(
        "retail/delete/<int:pk>/",
        Retail_networkDestroyAPIView.as_view(),
        name="retail-delete",
    ),
    path(
        "retail/update/<int:pk>/",
        Retail_networkUpdateAPIView.as_view(),
        name="retail-update",
    ),
]
