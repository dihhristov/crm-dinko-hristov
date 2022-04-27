from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from crm.accounts.models import Profile


class CreateProfileForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LEN,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LEN,
    )
    email = forms.EmailField()
    position = forms.ChoiceField(
        choices=Profile.POSITION,
    )
    image = forms.URLField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'position', 'image')

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            image=self.cleaned_data['image'],
            email=self.cleaned_data['email'],
            position=self.cleaned_data['position'],
            user=user,
        )

        if commit:
            profile.save()
            return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
