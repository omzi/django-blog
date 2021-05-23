from django.urls import path
from .views import RegisterView, UserEditView, PasswordChangeUserView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    path('change-password/', PasswordChangeUserView.as_view(), name='change-password'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html'), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset-password-done.html'), name='password_reset_done'),
    path('reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( template_name='registration/reset-password-confirm.html' ), name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset-password-complete.html'), name='password_reset_complete'),
]
