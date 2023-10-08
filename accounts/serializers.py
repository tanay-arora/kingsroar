from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

UserModel = get_user_model()

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)

# customer login
class newLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=15)

class OtpVerificationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,  max_length=15)
    password = serializers.CharField(style={'input_type': 'password'})
    otp = serializers.CharField(required=True)

class oldUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=15)
    password = serializers.CharField(style={'input_type': 'password'})

class oldUserOtpVerificationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=15)
    otp = serializers.CharField(required=True)

# seller login

class newSellerSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=25)
    username = serializers.CharField(required=True, max_length=15)
    otp = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})
