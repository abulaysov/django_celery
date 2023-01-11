from django.db.models import Prefetch, F, Sum
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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        response = super().list(request, *args, **kwargs)

        response_data = {'results': response.data}
        response_data['total_amount'] = queryset.aggregate(total=Sum('price')).get('total')
        response.data = response_data
        return response
