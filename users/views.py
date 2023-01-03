from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView
from users.forms import UserRegistrationForm


User = get_user_model()


class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'

    def get_success_url(self) -> str:
        return reverse('products:product-list')

    def post(self, request, *args, **kwargs):
        form = self.form_class()

        if form.is_valid():
            user = User(username=form.data['username'])
            user.set_password(form.data['password'])
            user.save()
            return redirect(self.get_success_url())
