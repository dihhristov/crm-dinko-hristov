from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as generic_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from crm.accounts import forms

from django.contrib.auth import login, get_user_model

from crm.accounts.forms import EditProfileForm
from crm.accounts.models import Profile

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    form_class = forms.CreateProfileForm
    success_url = reverse_lazy('show dashboard')
    template_name = 'accounts/register.html'

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(generic_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('show dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(generic_views.LogoutView):
    template_name = 'accounts/login.html'


class ChangePasswordView(generic_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ForgotPasswordView(generic_views.PasswordResetView):
    template_name = 'accounts/forgot-password.html'


def profile_details(request):
    profile = Profile.objects.get(pk=request.user.pk)
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile-details.html', context)


def edit_profile(request):
    if request.user.has_perm('accounts.change_profile'):
        profile = Profile.objects.get(pk=request.user.pk)
        if request.method == "POST":
            form = EditProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('show dashboard')
        form = EditProfileForm(instance=profile)
        context = {
            'profile': profile,
            'form': form,
        }
        return render(request, 'accounts/profile_edit.html', context)
    return redirect('show dashboard')