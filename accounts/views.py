from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from accounts.models import OTP
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.translation import ugettext_lazy as _

from .models import User, seller
from .serializers import OtpVerificationSerializer, TokenSerializer, newLoginSerializer, newSellerSerializer, oldUserLoginSerializer, oldUserOtpVerificationSerializer
from rest_framework.authtoken.models import Token

def create_token(user):
    token, _ = Token.objects.get_or_create(user=user)
    return token

class newLoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = newLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        username = self.request.data['username']

        try:
            if username.isdigit():
                user = User.objects.filter(username=username).exists()
                if(not user):
                    OTP.objects.filter(user=username).delete()
                    user = OTP.objects.create(user=username, otp='123456')
                    data = {
                        "mobile":username,
                        "otp_sent":True
                    }
                    response = Response(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'mobile': username,
                        'otp_sent': False,
                        'error': "You are already registered with us. Please log in."
                    }
                    response = Response(data, status=status.HTTP_200_OK)

            else:
                data = {
                    'mobile': username,
                    'otp_sent': False,
                    'error': "Please enter a valid Mobile Number."
                }
                response = Response(data, status=status.HTTP_200_OK)
        except:
            response = Response({"error":"Something went wrong here"}, status=status.HTTP_200_OK)
        return response

class OTPVerificationView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OtpVerificationSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        username = self.request.data['username']
        password = self.request.data['password']
        otp = self.request.data['otp']

        try:
            if username.isdigit() and otp.isdigit() and password:
                registered_user = User.objects.filter(username=username).exists()
                if not registered_user:
                    try:
                        uotp = OTP.objects.get(user=username)
                        if int(uotp.otp) == int(otp):
                                user, _ = User.objects.get_or_create(username=username,password=make_password(password),is_customer=True)
                                OTP.objects.filter(user=username).delete()
                                token = create_token(user)
                                serializer = TokenSerializer(instance=token, context={'request': self.request})
                                token_response = Response(serializer.data, status=status.HTTP_200_OK)
                                response = token_response
                        else:
                                data = {
                                    'mobile': username,
                                    'error': "OTP Mismatch"
                                    }
                                response = Response(data, status=status.HTTP_200_OK)

                    except OTP.DoesNotExist:
                        data = {
                            'mobile': username,
                            'error': "OTP is incorrect"
                            }
                        response = Response(data, status=status.HTTP_200_OK)
                else:
                    response = Response({'error': "You are already registered with us. Please login."}, status=status.HTTP_200_OK) 
            else:
                response = Response({"error":"Invalid username or password."}, status=status.HTTP_200_OK)    
        except:
            response = Response({"error":"Something went wrong here"}, status=status.HTTP_200_OK)
        return response

class oldUserLoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = oldUserLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        username = self.request.data['username']
        password = self.request.data['password']

        try:
            if username.isdigit() and password:
                registered_user = User.objects.filter(username=username).exists()
                if registered_user:
                    user = authenticate(username=username, password=password)
                    if user:
                        token = create_token(user)
                        serializer = TokenSerializer(instance=token, context={'request': self.request})
                        token_response = Response(serializer.data, status=status.HTTP_200_OK)
                        response = token_response
                    else:
                        response = Response({"error":"Invalid username or password."}, status=status.HTTP_200_OK)
                else:
                    response = Response({"error":"You are not registered with us. Please sign up."})
            else:
                response = Response({"error":"Invalid username or password."}, status=status.HTTP_200_OK)    
        except:
            response = Response({"error":"Something went wrong here."}, status=status.HTTP_200_OK)
        return response

class oldUserOtpSendView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = newLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        username = self.request.data['username']
        try:
            if username.isdigit():
                user = User.objects.filter(username=username).exists()
                if user:
                    OTP.objects.filter(user=username).delete()
                    user = OTP.objects.create(user=username, otp='123456')
                    data = {
                        "mobile":username,
                        "otp_sent":True
                    }
                    response = Response(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'mobile': username,
                        'otp_sent': False,
                        'error': "You are not registered with us. Please sign up."
                    }
                    response = Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    'mobile': username,
                    'otp_sent': False,
                    'error': "Please enter a valid Mobile Number."
                }
                response = Response(data, status=status.HTTP_200_OK)
        except:
            response = Response({"error":"Something went wrong here."}, status=status.HTTP_200_OK)
        return response

class oldUserOtpVerificaitonView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = oldUserOtpVerificationSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        username = self.request.data['username']
        otp = self.request.data['otp']

        try:
            if username.isdigit() and otp.isdigit():
                registered_user = User.objects.filter(username=username)
                if registered_user:
                    user = User.objects.get(username=username)
                    try:
                        uotp = OTP.objects.get(user=username)
                        if int(uotp.otp) == int(otp):
                            token = create_token(user)
                            serializer = TokenSerializer(instance=token, context={'request': self.request})
                            token_response = Response(serializer.data, status=status.HTTP_200_OK)
                            response = token_response
                        else:
                            response = Response({"error":"OTP Mismatch."})       
                    except:
                        response = Response({"error":"OTP not found, Please request for an otp again."})   
                else:
                    response = Response({"error":"You are not registered with us. Please sign up."})
            else:
                response = Response({"error":"Invalid username or otp."}, status=status.HTTP_200_OK)    
        except:
            response = Response({"error":"Something went wrong here."}, status=status.HTTP_200_OK)
        return response

class sellerSignUpview(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = newLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        username = self.request.data['username']

        try:
            if username.isdigit():
                user = User.objects.filter(username=username, is_seller=True).exists()
                if(not user):
                    OTP.objects.filter(user=username).delete()
                    user = OTP.objects.create(user=username, otp='123456')
                    data = {
                        "mobile":username,
                        "otp_sent":True
                    }
                    response = Response(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'mobile': username,
                        'otp_sent': False,
                        'error': "You are already registered with us. Please log in."
                    }
                    response = Response(data, status=status.HTTP_200_OK)

            else:
                data = {
                    'mobile': username,
                    'otp_sent': False,
                    'error': "Please enter a valid Mobile Number."
                }
                response = Response(data, status=status.HTTP_200_OK)
        except:
            response = Response({"error":"Something went wrong here"}, status=status.HTTP_200_OK)
        return response

class sellerSignupVerificationView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = newSellerSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        name = self.request.data['name']
        username = self.request.data['username']
        password = self.request.data['password']
        otp = self.request.data['otp']

        try:
            if username.isdigit() and otp.isdigit() and password and name:
                registered_user = User.objects.filter(username=username, is_seller=True).exists()
                if not registered_user:
                    try:
                        uotp = OTP.objects.get(user=username)
                        if int(uotp.otp) == int(otp):
                                User.objects.update_or_create(username=username,defaults={'first_name':name,'password':make_password(password),'is_customer':True,'is_seller':True})
                                user = User.objects.get(username=username, is_seller=True)
                                OTP.objects.filter(user=username).delete()
                                token = create_token(user)
                                serializer = TokenSerializer(instance=token, context={'request': self.request})
                                token_response = Response(serializer.data, status=status.HTTP_200_OK)
                                response = token_response
                        else:
                                data = {
                                    'mobile': username,
                                    'error': "OTP Mismatch"
                                    }
                                response = Response(data, status=status.HTTP_200_OK)

                    except OTP.DoesNotExist:
                        data = {
                            'mobile': username,
                            'error': "OTP is incorrect"
                            }
                        response = Response(data, status=status.HTTP_200_OK)
                else:
                    response = Response({'error': "You are already registered with us. Please login."}, status=status.HTTP_200_OK) 
            else:
                response = Response({"error":"Invalid username or password."}, status=status.HTTP_200_OK)    
        except:
            response = Response({"error":"Something went wrong here"}, status=status.HTTP_200_OK)
        return response


class oldSellerLoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = oldUserLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        username = self.request.data['username']
        password = self.request.data['password']

        try:
            if username.isdigit() and password:
                registered_user = User.objects.filter(username=username, is_seller=True).exists()
                if registered_user:
                    user = authenticate(username=username, password=password)
                    if user:
                        token = create_token(user)
                        serializer = TokenSerializer(instance=token, context={'request': self.request})
                        token_response = Response(serializer.data, status=status.HTTP_200_OK)
                        response = token_response
                    else:
                        response = Response({"error":"Invalid username or password."}, status=status.HTTP_200_OK)
                else:
                    response = Response({"error":"You are not registered with us. Please sign up."})
            else:
                response = Response({"error":"Invalid username or password."}, status=status.HTTP_200_OK)    
        except:
            response = Response({"error":"Something went wrong here."}, status=status.HTTP_200_OK)
        return response

class oldSellerOtpSendView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = newLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        username = self.request.data['username']
        try:
            if username.isdigit():
                user = User.objects.filter(username=username, is_seller=True).exists()
                if user:
                    OTP.objects.filter(user=username).delete()
                    user = OTP.objects.create(user=username, otp='123456')
                    data = {
                        "mobile":username,
                        "otp_sent":True
                    }
                    response = Response(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'mobile': username,
                        'otp_sent': False,
                        'error': "You are not registered with us. Please sign up."
                    }
                    response = Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    'mobile': username,
                    'otp_sent': False,
                    'error': "Please enter a valid Mobile Number."
                }
                response = Response(data, status=status.HTTP_200_OK)
        except:
            response = Response({"error":"Something went wrong here."}, status=status.HTTP_200_OK)
        return response

class oldSellerOtpVerificaitonView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = oldUserOtpVerificationSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        username = self.request.data['username']
        otp = self.request.data['otp']

        try:
            if username.isdigit() and otp.isdigit():
                registered_user = User.objects.filter(username=username, is_seller=True)
                if registered_user:
                    user = User.objects.get(username=username, is_seller=True)
                    try:
                        uotp = OTP.objects.get(user=username)
                        if int(uotp.otp) == int(otp):
                            token = create_token(user)
                            serializer = TokenSerializer(instance=token, context={'request': self.request})
                            token_response = Response(serializer.data, status=status.HTTP_200_OK)
                            response = token_response
                        else:
                            response = Response({"error":"OTP Mismatch."})       
                    except:
                        response = Response({"error":"OTP not found, Please request for an otp again."})   
                else:
                    response = Response({"error":"You are not registered with us. Please sign up."})
            else:
                response = Response({"error":"Invalid username or otp."}, status=status.HTTP_200_OK)    
        except:
            response = Response({"error":"Something went wrong here."}, status=status.HTTP_200_OK)
        return response


class forgetPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = newLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        
        username = self.request.data['username']

        try:
            if username.isdigit():
                user = User.objects.filter(username=username).exists()
                if user:
                    OTP.objects.filter(user=username).delete()
                    user = OTP.objects.create(user=username, otp='123456')
                    data = {
                        "mobile":username,
                        "otp_sent":True
                    }
                    response = Response(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'mobile': username,
                        'otp_sent': False,
                        'error': "You are not registered with us. Please sign up."
                    }
                    response = Response(data, status=status.HTTP_200_OK)

            else:
                data = {
                    'mobile': username,
                    'otp_sent': False,
                    'error': "Please enter a valid Mobile Number."
                }
                response = Response(data, status=status.HTTP_200_OK)
        except:
            response = Response({"error":"Something went wrong here"}, status=status.HTTP_200_OK)
        return response

class forgetPasswordVerificationView(GenericAPIView):   
    permission_classes = (AllowAny,)
    serializer_class = OtpVerificationSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        
        username = self.request.data['username']
        password = self.request.data['password']
        otp = self.request.data['otp']

        try:
            if username.isdigit() and otp.isdigit() and password:
                registered_user = User.objects.filter(username=username).exists()
                if registered_user:
                    try:
                        uotp = OTP.objects.get(user=username)
                        if int(uotp.otp) == int(otp):
                                user, _ = User.objects.update_or_create(username=username, defaults={"password":make_password(password)})
                                OTP.objects.filter(user=username).delete()
                                token = create_token(user)
                                serializer = TokenSerializer(instance=token, context={'request': self.request})
                                token_response = Response(serializer.data, status=status.HTTP_200_OK)
                                response = token_response
                        else:
                                data = {
                                    'mobile': username,
                                    'error': "OTP Mismatch"
                                    }
                                response = Response(data, status=status.HTTP_200_OK)

                    except OTP.DoesNotExist:
                        data = {
                            'mobile': username,
                            'error': "OTP is incorrect"
                            }
                        response = Response(data, status=status.HTTP_200_OK)
                else:
                    response = Response({'error': "You are not registered with us. Please sign up."}, status=status.HTTP_200_OK) 
            else:
                response = Response({"error":"Invalid username or password."}, status=status.HTTP_200_OK)    
        except:
            response = Response({"error":"Something went wrong here"}, status=status.HTTP_200_OK)
        return response

class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass
        response = Response({"detail":"Successfully logged out."},status=status.HTTP_200_OK)
        return response