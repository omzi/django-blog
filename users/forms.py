from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=4, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter A Username'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Address'}))
    first_name = forms.CharField(label='First Name', min_length=4, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Your First Name'}))
    last_name = forms.CharField(label='Last Name', min_length=4, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Last Name'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserEditForm(UserChangeForm):
    username = forms.CharField(label='Username', min_length=4, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter A Username', 'class': 'input-form trans-bg'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Address', 'class': 'input-form trans-bg'}))
    first_name = forms.CharField(label='First Name', min_length=4, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Your First Name', 'class': 'input-form trans-bg'}))
    last_name = forms.CharField(label='Last Name', min_length=4, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Last Name', 'class': 'input-form trans-bg'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       del self.fields['password']


class PasswordChangeUserForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your New Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your New Password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class PasswordResetUserForm(PasswordResetForm):
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Address'}))

    class Meta:
        model = User
        fields = ('email')


class PasswordConfirmUserForm(PasswordResetForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your New Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your New Password'}))

    class Meta:
        model = User
        fields = ('email')