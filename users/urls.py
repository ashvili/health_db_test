from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import SignUpView, LoginUserView, logout_user, AsdUserChangeView, PasswordChangeView


app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', login_required(logout_user), name='logout'),
    path('profile/<int:pk>/', login_required(AsdUserChangeView.as_view()), name='profile'),
    path('password_change/', login_required(PasswordChangeView.as_view()), name='password_change'),
]