from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(forms.ModelForm):
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    # class Meta:
    #     model = Profile
    #     fields = ['avatar']

    # avatar = forms.ImageField(
    #     required=False,
    #     widget=forms.FileInput(attrs={'class': 'form-control-file'})
    # )

    avatar_url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter avatar URL'})
    )

    class Meta:
        model = Profile
        fields = ['avatar_url']