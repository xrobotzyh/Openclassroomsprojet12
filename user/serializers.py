from rest_framework import serializers

from .models import User


class UserInscriptionSerializer(serializers.ModelSerializer):
    # register serializer
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label='Confirm password')

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'password',
                  'password2',
                  'first_name',
                  'last_name',
                  'email',
                  'telephone',
                  'department']
        read_only_fields = ['id']

    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        if password2 != password1:
            raise serializers.ValidationError({'password2': 'You must enter the same password.'})
        attrs.pop('password2')
        return attrs

    # rewrite the create method to encrypt the password
    def create(self, validated_data):
        password = validated_data['password']
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_full_name(self,validated_data):
        full_name = validated_data.first_name + '' + validated_data.last_name
        return full_name

