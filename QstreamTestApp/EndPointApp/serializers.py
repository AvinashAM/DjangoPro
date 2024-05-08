from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email_address', 'country']

    def validate_country(self, value):
        if value and value not in ['Ireland', 'United States']:
            raise serializers.ValidationError("Country must be either 'Ireland' or 'United States'")
        return value