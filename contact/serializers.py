from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    # register serializer
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['id', 'contact', 'created_at', 'updated_at']
