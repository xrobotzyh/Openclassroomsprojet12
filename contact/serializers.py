from rest_framework import serializers

from .models import Client, ClientContact


class CreateClientSerializer(serializers.ModelSerializer):
    # register serializer
    class Meta:
        model = Client
        fields = ['id',
                  'first_name',
                  'last_name',
                  'contact_user',
                  'email',
                  'telephone',
                  'enterprise_name',
                  'created_at',
                  'updated_at']
        read_only_fields = ['id', 'contact_user', 'created_at', 'updated_at', 'contact_user']
