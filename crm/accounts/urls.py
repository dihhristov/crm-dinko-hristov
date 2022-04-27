from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from crm.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ChangePasswordView, ForgotPasswordView, \
    edit_profile, profile_details

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('change-password', ChangePasswordView.as_view(), name='change password'),
    path('change_password_done/', RedirectView.as_view(url=reverse_lazy('show dashboard')),
         name='password change done'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot password'),

    path('profile-details', profile_details, name='profile details'),
    path('profile-edit/', edit_profile, name='edit profile'),
)
