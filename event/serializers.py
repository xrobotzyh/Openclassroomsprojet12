from rest_framework import serializers

from contact.models import Client
from user.models import User
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    # register serializer
    client_name = serializers.SerializerMethodField(read_only=True)
    client_contact = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['id', 'starts_at', 'updated_at', 'client_name', 'client_contact']

    def get_client_name(self, obj):
        return obj.client.first_name + ' ' + obj.client.last_name

    def get_client_contact(self, obj):
        return obj.client.email + ' ' + obj.client.phone

    def validate(self, data):
        contract = data.get('contrat')
        assign_to_user = data.get('assigned_to')

        if contract.status == 'not_sign':
            raise serializers.ValidationError('The contract has not signed, please wait the client to sign it')

        if Client.objects.get(id=contract.client_id).contact_id != self.context['request'].user.id:
            raise serializers.ValidationError('You do not have permission to create the event')

        if not assign_to_user.is_support():
            raise serializers.ValidationError('Assignee must be a support user.')

        return data
