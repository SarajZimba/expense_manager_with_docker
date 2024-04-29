from rest_framework import serializers
from user.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}  # To ensure password isn't returned in responses

    def create(self, validated_data):
        user = Customer.objects.create_user(**validated_data)
        return user
    


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import Customer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        # Add any other custom data you want to include in the token
        data['email'] = self.user.email  # Include email if needed
        return data

