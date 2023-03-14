from django import forms
from django.contrib.auth import get_user_model

from common.forms import BaseForm


User = get_user_model()


class UserRegistrationForm(BaseForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        label='Электронная почта',
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        label='Имя пользователя',
    )
    password = forms.CharField(
        max_length=100,
        required=True,
        label='Пароль',
        widget=forms.PasswordInput(),
    )
    confirm_password = forms.CharField(
        max_length=100,
        required=True,
        label='Повторите пароль',
        widget=forms.PasswordInput(),
    )
