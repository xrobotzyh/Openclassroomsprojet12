from rest_framework import serializers

from .models import Contract


class CreateContractSerializer(serializers.ModelSerializer):
    # register serializer
    client_name = serializers.SerializerMethodField(read_only=True)
    client_from_seller = serializers.StringRelatedField(source="client_id.contact_id")

    class Meta:
        model = Contract
        fields = ['id',
                  'client_name',
                  'client_id',
                  'client_from_seller',
                  'quotation',
                  'paid',
                  'status',
                  'created_at',
                  'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'client_from_seller']

    def get_client_name(self, obj):
        client_name = obj.client_id.first_name + ' ' + obj.client_id.last_name
        return client_name
