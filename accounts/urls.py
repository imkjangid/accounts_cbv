from django.urls import path
from .views import *

urlpatterns = [
    path('login-gate/', LoginGate.as_view(), name='login-gate'),
    path('registration-gate/', RegistrationGate.as_view(), name='registration-gate'),
    path('register-user/', RegisterUser.as_view(), name='register-gate'),
    path('profile-gate/', ProfileGate.as_view(), name='profile-gate'),
    path('user-profile/', ProfileView.as_view(), name='user-profile'),
]