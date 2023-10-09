from rest_framework import serializers

from .models import Contract


class CreateContractSerializer(serializers.ModelSerializer):
    # register serializer
    client_name = serializers.SerializerMethodField()
    client_from_seller = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['id',
                  'client_name',
                  'client',
                  'client_from',
                  'client_from_seller',
                  'name',
                  'quotation',
                  'status',
                  'created_at',
                  'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_client_name(self, obj):
        client_name = obj.Client.first_name + '' + obj.Client.last_name
        return client_name

    def get_client_from_seller(self, obj):
        return obj.Client.contact_user_id
