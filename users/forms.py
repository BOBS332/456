from django.forms.models import ModelForm

from .models import User


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
