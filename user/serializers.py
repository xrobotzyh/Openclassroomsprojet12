from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
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
                  'phone',
                  'department']
        read_only_fields = ['id']

    # rewrite the create method to encrypt the password
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')

        if password2 != password1:
            raise serializers.ValidationError({'password2': 'You must enter the same password.'})

        attrs.pop('password2')
        return attrs

    # re write the create method to encrypt the password
    def create(self, validated_data):
        password = validated_data['password']

        user = self.Meta.model(**validated_data)

        user.set_password(password)

        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        # Update other fields as needed
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # If a new password is provided, set and save it
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


