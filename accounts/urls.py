from django.urls import path, include
from .views import *

urlpatterns = [
    path('c/signup/', newLoginView.as_view(), name='Customer signup'),
    path('c/signup/confirm/', OTPVerificationView.as_view(), name="Customer signup otp verification"),
    path('c/login/', oldUserLoginView.as_view(), name="Customer login"),
    path('c/otp-login/', oldUserOtpSendView.as_view(), name="Customer Login with otp"),
    path('c/otp-login/confirm/', oldUserOtpVerificaitonView.as_view(), name="Customer login Otp verification"),
    path('s/signup/', sellerSignUpview.as_view(), name="Seller signup"),
    path('s/signup/confirm/', sellerSignupVerificationView.as_view(), name="seller otp verification"),
    path('s/login/', oldSellerLoginView.as_view(), name="Seller login"),
    path('s/otp-login/', oldSellerOtpSendView.as_view(), name="Seller Login with otp"),
    path('s/otp-login/confirm/', oldSellerOtpVerificaitonView.as_view(), name="Seller login otp verification"),
    path('forgot-password/', forgetPasswordView.as_view(), name="Forgot password customer/seller"),
    path('forgot-password/confirm/', forgetPasswordVerificationView.as_view(), name="Forgot password confirm customer/seller"),
    path('logout/', LogoutView.as_view(), name="Logout customer/seller")
]