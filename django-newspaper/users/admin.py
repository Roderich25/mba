from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'birthday', 'is_staff']
    fieldsets = (
                (None, {'fields': ()}),
                ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'email', 'birthday')})
            )


admin.site.register(CustomUser, CustomUserAdmin)
