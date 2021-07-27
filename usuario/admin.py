from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email', 'admin','profile' ]
    list_filter = ['admin','profile','staff', 'is_active',]
    fieldsets = (
        (None, {'fields': ('profile','email', 'password',)}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin','staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_2')}
        ),
    )
    search_fields = ['email', 'is_staff', 'is_active', ]
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

