from collections import defaultdict
from typing import ClassVar, Optional

from users.models import User


class UserService:
    _model: ClassVar[type[User]] = User

    def check_user_exists(self, **filters) -> bool:
        return self._model.objects.filter(**filters).exists()

    def register_user(
        self,
        email: str,
        username: str,
        password: str,
        confirm_password: str,
    ) -> tuple[Optional[User], dict]:
        errors = defaultdict(list)

        if self.check_user_exists(email=email):
            errors['email'].append('Пользователь с таким email уже зарегестрирован')
        new_user = None

        # TODO: остальные валидации

        if len(errors) == 0:
            new_user = self.create_user(
                email=email,
                username=username,
                password=password,
            )
        return new_user, errors
