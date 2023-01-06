from rest_framework import viewsets
from services import models
from services import serializers


class SubscriptionView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
