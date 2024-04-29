from django.urls import path
from api.views.user import RegisterUserAPIView, LoginUserAPIView,ForgotPasswordAPIView, ResetPasswordAPIView, CustomTokenObtainPairView



urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
     path('forgot_password/', ForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('reset_password/<str:token>/', ResetPasswordAPIView.as_view(), name='reset_password'),
    path('token/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

]
