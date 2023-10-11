from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    # register serializer
    class Meta:
        model = Client
        fields = ['id',
                  'contact_id',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'company_name',
                  'created_at',
                  'updated_at']
        read_only_fields = ['id', 'contact_id', 'created_at', 'updated_at']
