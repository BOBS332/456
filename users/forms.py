# from django.forms.models import ModelForm
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Имя пользователя')
    password = forms.CharField(max_length=100, required=True, label='Пароль', widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=100, required=True, label='Повторите пароль',
                                       widget=forms.PasswordInput())

    def clean_username(self):
        if User.objects.filter(username=self.data['username']).exists():
            raise ValidationError('Пользоватлеь с таким именем уже существует')

    class Meta:
        model = User
