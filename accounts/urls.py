from django.urls import path
from accounts.views import login_attempt, register_attempt, success, token_send

urlpatterns = [
	path('login/', login_attempt, name="login"),
	path('register/', register_attempt, name="register"),
	path('success/', success, name="success"),
	path('token/', token_send, name="token_send"),
]