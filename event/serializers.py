from rest_framework import serializers

from user.models import User
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    # register serializer
    client_name = serializers.SerializerMethodField(read_only=True)
    client_contact = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = ['id',
                  'contrat_id',
                  'client_name',
                  'client_contact',
                  'assigned_to',
                  'starts_at',
                  'ends_at',
                  'location',
                  'attendees',
                  'notes']
        read_only_fields = ['id', 'starts_at', 'updated_at', 'client_name', 'client_contact']

    def get_client_name(self, obj):
        return obj.client_id.first_name + ' ' + obj.client_id.last_name

    def get_client_contact(self, obj):
        return obj.client_id.email + ' ' + obj.client_id.phone

    def validate_assigned_to(self, value):
        user = User.objects.get(id=value.id)
        if not user.department == 'support':
            raise serializers.ValidationError("Assignee must be a support user.")
