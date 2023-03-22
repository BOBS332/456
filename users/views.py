from django.contrib.auth import get_user_model
from django.http.request import HttpRequest

from django.urls import reverse
from django.views.generic import FormView

from users.forms import UserRegistrationForm
from users.services.user_service import UserService


User = get_user_model()


class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'

    def get_success_url(self) -> str:
        return reverse('index')

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(data=request.POST)
        user_service = UserService()

        if form.is_valid():
            _, errors = user_service.register_user(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                confirm_password=form.cleaned_data['confirm_password'],
            )

            if len(errors) > 0:
                form.add_errors(errors)
                return self.form_invalid(form)

            return self.form_valid(form)
        return self.form_invalid(form)


# TODO: Написать форму для логина
# написать логику авторизации через сервис
# если ошибок у пользователя нет авторизуем его
# если ошибки есть, показываем через .add_errors и return form_invalid(form)
class UserLoginView(FormView):
    ...
