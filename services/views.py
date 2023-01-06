from django.db.models import Prefetch
from rest_framework import viewsets

from clients.models import Client
from services import models
from services import serializers


class SubscriptionView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client',
                 queryset=Client.objects.all().select_related('user')
                 .only('company_name',
                       'user__email')
                 )
    )
    serializer_class = serializers.SubscriptionSerializer
