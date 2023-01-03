from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from users.models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    list_display = (('username', 'email', 'full_name', 'rating'))

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('rating',)}),
    )


admin.site.register(User, MyUserAdmin)