# authentication.py

from django.contrib.auth.backends import BaseBackend
from .models import Customer

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Customer.objects.get(username=username)
            if user.check_password(password):
                return user
        except Customer.DoesNotExist:
            return None
        
from rest_framework_simplejwt.authentication import JWTAuthentication
# from user.models import Customer

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get('user_id')
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None

