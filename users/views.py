from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from home.models import Category
from .forms import RegistrationForm, UserEditForm, PasswordChangeUserForm
from django.contrib import messages


class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.warning(self.request, "You're already logged in!")
            return redirect('home')
        return super(RegisterView, self).get(request, *args, **kwargs)


class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('home')
    extra_context = {'categories': Category.objects.all()}

    def get_object(self):
        return self.request.user


class PasswordChangeUserView(PasswordChangeView):
    form_class = PasswordChangeUserForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')
