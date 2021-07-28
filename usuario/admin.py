from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile
from .forms import UserAdminCreationForm, UserAdminChangeForm, ProfileForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email', 'admin', 'profile', 'active', 'staff' ]
    list_filter = ['admin','profile','staff', 'active',]
    fieldsets = (
        (None, {'fields': ('profile','email', 'password',)}),
        ('Permissões', {'fields': ('admin','staff', 'active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_2')}
        ),
    )
    search_fields = ['email', 'profile', 'staff', 'active', ]
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# class UserAdmin2(admin.ModelAdmin):

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    add_form = ProfileForm

    list_display = ['name', 'date_joined', ]
    list_filter = ['name', 'date_joined',]
    fieldsets = (
        (None, {'fields': ('email', 'name', 'photograph',)}),
        ('Informações Pessoais', {'fields': ('cpf', 'doc_id',)}),
        ('Endereço', {'fields': ('street','number', 'compl', 'neighbor', 'city',)}),
        ('Dados Profissional', {'fields': ('category','curriculum',)}),
        ('Termo de concordância', {'fields': ('terms',)}),
    )
    readonly_fields = ['view_image',]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('photograph', 'name', 'photograph',),
            'Informações Pessoais': ('cpf', 'doc_id',),
            'Endereço': ('street','number', 'compl', 'neighbor', 'city',),
            'Dados Profissional': ('category','curriculum',),
            'Termo de concordância': ('terms',)}
        ),
    )
    search_fields = ['name']
    ordering = ['name']
    filter_horizontal = ()    


admin.site.register(Profile, ProfileAdmin)


