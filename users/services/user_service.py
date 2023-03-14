from collections import defaultdict
from typing import Optional, ClassVar
from users.models import User



class UserService:
    __model: ClassVar[type[User]] = User

    def check_user_exists(self, **filters) -> bool:
        return self.__model.objects.filter(**filters).exists()

    def register_user(self,
        email: str,
        username: str,
        password: str,
        confirm_password: str,
    ) -> tuple[Optional[User], dict]:
        errors = defaultdict(list)
        if self.check_user_exists(email=email):
            errors['email'].append('Пользователь с таким email уже зарегестрирован')
        new_user = None

        if self.check_user_exists(username=username):
            errors['username'].append('Пользователь с таким именем уже существует')

        if self.check_user_exists(password=password, confirm_password=confirm_password):
            if password != confirm_password:
                errors['password'].append('Пароли не совпадают')
            if len(password) < 8:
                errors['password'].append('Слишком короткий пароль')

        if len(errors) == 0:
            new_user = self.create_user(
                email=email,
                username=username,
                password=password,
                confirm_password=confirm_password,
            )
            return new_user, errors

