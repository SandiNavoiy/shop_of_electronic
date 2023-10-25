from django.urls import path

from factory.apps import FactoryConfig
from factory.views import FactoryListAPIView, FactoryCreateAPIView, FactoryRetrieveAPIView, FactoryDestroyAPIView, \
    FactoryUpdateAPIView

app_name = FactoryConfig.name


urlpatterns = [
    path("factory/", FactoryListAPIView.as_view(), name="factory-list"),
    path("factory/create/", FactoryCreateAPIView.as_view(), name="factory-create"),
    path("factory/detail/<int:pk>/", FactoryRetrieveAPIView.as_view(), name="factory-detail"),
    path("factory/delete/<int:pk>/", FactoryDestroyAPIView.as_view(), name="factory-delete"),
    path("factory/update/<int:pk>/", FactoryUpdateAPIView.as_view(), name="factory-update"),
]