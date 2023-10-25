from django.urls import path

from links.apps import LinksConfig
from links.views import LinkCreateAPIView, LinkRetrieveAPIView, LinkDestroyAPIView, LinkUpdateAPIView

app_name = LinksConfig.name


urlpatterns = [

    path("links/create/", LinkCreateAPIView.as_view(), name="links-create"),
    path("links/detail/<int:pk>/", LinkRetrieveAPIView.as_view(), name="links-detail"),
    path("links/delete/<int:pk>/", LinkDestroyAPIView.as_view(), name="links-delete"),
    path("links/update/<int:pk>/", LinkUpdateAPIView.as_view(), name="links-update"),
]