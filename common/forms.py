from django.forms import Form


class BaseForm(Form):
    def add_errors(self, errors: dict[str, list[str]]) -> None:
        for field, errors_list in errors.items():
            for error in errors_list:
                self.add_error(field, error)
